import React, { RefObject, ChangeEvent } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { UploadHelper, UploadPayload, ModelsInfo } from "../utils/UploadHelper";
import { RestErrors } from "../utils/RestHelper";
import { LiteEvent } from "../utils/EventHandler";
import { IconPrefix, IconName } from "@fortawesome/fontawesome-svg-core";
import * as settings from "../settings/settings.json";


interface FileUploadProps {
}
interface FileUploadState {
    uploadIcon: [IconPrefix, IconName];
    spinUploadIcon: boolean;
    uploadInfoText: string;
    enableUpload: boolean;
    modelValue: string;
    modelsInfo: typeof settings.models
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
             enableUpload: true,
             modelValue: 'colornet',
             modelsInfo: settings.models
            };
    }

    componentDidMount() {
        this.getModels();
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
        this.uploadHelper.handleUpload(this.fileInputRef.current?.files, this.state.modelValue)
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

    private handleChange(e: ChangeEvent<HTMLSelectElement>) {
        e.persist();
        this.setState({ modelValue: e.target.value });
    }

    private getModels() {
        this.uploadHelper.getModels()
        .then((e) => {
            e = (e as ModelsInfo);
            if(e && e.strategies) {
                this.setState({modelsInfo: e.strategies});
            }
        })
        .catch((e: RestErrors) => {
            console.error(this.getErrorMessage(e)); // silently drop this error
        })
    }

    handleUpload(e: React.MouseEvent<HTMLButtonElement, MouseEvent>): void {
        e.preventDefault();
        this.startUpload();
    }

    getErrorMessage(e: RestErrors): string {
        switch(e) {
            case RestErrors.BackendUnavailable:
                return "We couldn't find our server... thats unfortunate. Please come back later!";
            case RestErrors.MalformedJson:
                return "We couldn't decipher our server's gibberish. Please contact us if this error persists";
            case RestErrors.MissingPayload:
                return "You might have forgotten to select an image file. Please do so!";
        }
    }

    displayError(e: RestErrors) {
        if(!this.errorMessage.current) return;
        this.errorMessage.current.style.display = "block";

        this.errorMessage.current.innerHTML = this.getErrorMessage(e);
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
                    <select
                        value={this.state.modelValue}
                        onChange={(e) => { this.handleChange(e); }}
                    >
                        {this.state.modelsInfo.map((model, i) => {
                            return (<option value={model.var} key={i}>{model.name}</option>)
                        })}
                    </select>
                    <button onClick={(e) => this.handleUpload(e)}><FontAwesomeIcon icon={this.state.uploadIcon} spin={this.state.spinUploadIcon}/></button>
                </div>
            </div>);
    }
}