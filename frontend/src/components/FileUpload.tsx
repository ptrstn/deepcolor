import React, { RefObject } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { UploadHelper, UploadPayload } from "../utils/UploadHelper";
import { RestErrors } from "../utils/RestHelper";
import { LiteEvent } from "../utils/EventHandler";
import { IconPrefix, IconName } from "@fortawesome/fontawesome-svg-core";


interface FileUploadProps {
}
interface FileUploadState {
    uploadIcon: [IconPrefix, IconName];
    spinUploadIcon: boolean;
    uploadInfoText: string;
    enableUpload: boolean;
}

export class FileUpload extends React.Component<FileUploadProps, FileUploadState> {
    private readonly fileInputRef: RefObject<HTMLInputElement> = React.createRef();
    private readonly outerWrapper: RefObject<HTMLDivElement> = React.createRef();
    private readonly errorMessage: RefObject<HTMLDivElement> = React.createRef();
    private readonly uploadHelper: UploadHelper = new UploadHelper();
    private readonly uploadListener = new LiteEvent<UploadPayload>();

    constructor(props: FileUploadProps) {
        super(props);
        this.state = {
            uploadIcon: ['fas', 'cloud-upload-alt'],
             spinUploadIcon: false,
             uploadInfoText: "Choose a file",
             enableUpload: true
            };
    }

    private handleFileInputChange(event: React.ChangeEvent<HTMLInputElement>) {
        if(this.fileInputRef.current) {
            this.setState({uploadInfoText: this.fileInputRef.current.value.split("\\").pop() ?? "unknown"});
            this.startUpload();
        }
    }

    private toogleUpload() {
        if(this.state.enableUpload)
            this.setState({uploadIcon: ["fas", "cog"], spinUploadIcon: true, enableUpload: false});
        else
            this.setState({uploadIcon: ["fas", "cloud-upload-alt"], spinUploadIcon: false, enableUpload: true});
    }

    private startUpload() {
        this.toogleUpload();
        this.uploadHelper.handleUpload(this.fileInputRef.current?.files)
        .then((e) => {
            this.toogleUpload();
            this.outerWrapper.current?.classList.add("input-success");
            this.uploadListener.trigger(e as UploadPayload);
        })
        .catch((e) => {
            this.toogleUpload();
            this.outerWrapper.current?.classList.add("input-error");
            this.displayError(e);
        })
    }

    handleUpload(e: React.MouseEvent<HTMLButtonElement, MouseEvent>): void {
        e.preventDefault();
        this.startUpload();
    }
    displayError(e: RestErrors) {
        if(!this.errorMessage.current) return;
        this.errorMessage.current.style.display = "block";

        switch(e) {
            case RestErrors.BackendUnavailable:
                this.errorMessage.current.innerHTML = "We couldn't find our server... thats unfortunate. Please come back later!"
                break;
            case RestErrors.MalformedJson:
                this.errorMessage.current.innerHTML = "We couldn't decipher our server's gibberish. Please contant us if this error persists"
                break;
            case RestErrors.MissingPayload:
                this.errorMessage.current.innerHTML = "You might have forgotten to select an image file. Please do so!"
                break;
        }
    }

    public get uploadEvent() { return this.uploadListener.expose() }

    render() {
        return (
            <div>
                <div className="error-message" ref={this.errorMessage}></div>
                <div className="upload-input" ref={this.outerWrapper}>
                    <label>
                        <input type="file" name="file" id="file" className="inputfile" ref={this.fileInputRef} onChange={(e) => this.handleFileInputChange(e)} disabled={!this.state.enableUpload}/>
                        <span>{this.state.uploadInfoText}</span>
                    </label>
                    <button onClick={(e) => this.handleUpload(e)}><FontAwesomeIcon icon={this.state.uploadIcon} spin={this.state.spinUploadIcon}/></button>
                </div>
            </div>);
    }
}