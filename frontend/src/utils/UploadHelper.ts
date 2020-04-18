import { RefObject } from "react";

export class UploadHelper {
    private uploadInput: RefObject<HTMLInputElement>;

    constructor(uploadInput: RefObject<HTMLInputElement>) {
        this.uploadInput = uploadInput;
    }

    handleUpload(e: import("react").MouseEvent<HTMLButtonElement, MouseEvent>): Promise<string> {
        return new Promise(
            (resolve, reject) => {
                e.preventDefault();
                if(!this.uploadInput.current || !this.uploadInput.current.files) {
                    reject("Missing File!");
                    return;
                }

                let file = this.uploadInput.current.files[0];
                let formData = new FormData();
                formData.append('file', file);

                let request = new XMLHttpRequest();
                request.open("POST", "/api/v1/image");
                request.addEventListener('load', function(event) {
                    if (request.status >= 200 && request.status < 300) {
                        resolve();
                    } else {
                        reject(request.statusText);
                    }
                });
                request.send(formData);
        });
    }
}