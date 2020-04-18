import React, { RefObject } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { UploadHelper } from "../utils/UploadHelper";


interface FileUploadProps {
}
interface FileUploadState {
}

export class FileUpload extends React.Component<FileUploadProps, FileUploadState> {
    private fileInputRef: RefObject<HTMLInputElement> = React.createRef();
    private fileInputInfo: RefObject<HTMLSpanElement> = React.createRef();
    private outerWrapper: RefObject<HTMLDivElement> = React.createRef();
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
            console.warn(e);
        })
    }

    render() {
        return (
            <div className="upload-input" ref={this.outerWrapper}>
                <label>
                    <input type="file" name="file" id="file" className="inputfile" ref={this.fileInputRef} onChange={(e) => this.handleFileInputChange(e)}/>
                    <span ref={this.fileInputInfo}>Choose a file</span>
                </label>
                <button onClick={(e) => this.handleUpload(e)}><FontAwesomeIcon icon={['fas', 'cloud-upload-alt']} /></button>
            </div>);
    }
}