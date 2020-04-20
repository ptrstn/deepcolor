import React, { RefObject } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { UploadHelper, UploadPayload } from "../utils/UploadHelper";
import { RestErrors } from "../utils/RestHelper";
import { LiteEvent } from "../utils/EventHandler";


interface FileUploadProps {
}
interface FileUploadState {
}

export class FileUpload extends React.Component<FileUploadProps, FileUploadState> {
    private readonly fileInputRef: RefObject<HTMLInputElement> = React.createRef();
    private readonly fileInputInfo: RefObject<HTMLSpanElement> = React.createRef();
    private readonly outerWrapper: RefObject<HTMLDivElement> = React.createRef();
    private readonly errorMessage: RefObject<HTMLDivElement> = React.createRef();
    private readonly uploadHelper: UploadHelper = new UploadHelper();
    private readonly uploadListener = new LiteEvent<UploadPayload>();

    private handleFileInputChange(event: React.ChangeEvent<HTMLInputElement>) {
        if(this.fileInputInfo.current && this.fileInputRef.current) {
            this.fileInputInfo.current.innerHTML = this.fileInputRef.current.value.split("\\").pop() ?? "unknown";
        }
    }

    handleUpload(e: React.MouseEvent<HTMLButtonElement, MouseEvent>): void {
        e.preventDefault();

        this.uploadHelper.handleUpload(this.fileInputRef.current?.files)
        .then((e) => {
            this.uploadListener.trigger(e as UploadPayload);
        })
        .catch((e) => {
            this.outerWrapper.current?.classList.add("input-error");
            this.displayError(e);
        })
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
                        <input type="file" name="file" id="file" className="inputfile" ref={this.fileInputRef} onChange={(e) => this.handleFileInputChange(e)}/>
                        <span ref={this.fileInputInfo}>Choose a file</span>
                    </label>
                    <button onClick={(e) => this.handleUpload(e)}><FontAwesomeIcon icon={['fas', 'cloud-upload-alt']} /></button>
                </div>
            </div>);
    }
}