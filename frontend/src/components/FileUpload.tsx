import React, { RefObject } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { UploadHelper } from "../utils/UploadHelper";
import { RestErrors } from "../utils/RestHelper";


interface FileUploadProps {
}
interface FileUploadState {
}

export class FileUpload extends React.Component<FileUploadProps, FileUploadState> {
    private fileInputRef: RefObject<HTMLInputElement> = React.createRef();
    private fileInputInfo: RefObject<HTMLSpanElement> = React.createRef();
    private outerWrapper: RefObject<HTMLDivElement> = React.createRef();
    private errorMessage: RefObject<HTMLDivElement> = React.createRef();
    private uploadHelper: UploadHelper = new UploadHelper(this.fileInputRef);

    private handleFileInputChange(event: React.ChangeEvent<HTMLInputElement>) {
        if(this.fileInputInfo.current && this.fileInputRef.current) {
            this.fileInputInfo.current.innerHTML = this.fileInputRef.current.value.split("\\").pop() ?? "unknown";
        }
    }

    handleUpload(e: React.MouseEvent<HTMLButtonElement, MouseEvent>): void {
        this.uploadHelper.handleUpload(e)
        .then(() => { console.log("Success!") })
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