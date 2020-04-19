import { RefObject } from "react";
import { RestErrors, RestHelper, RestMethods } from "./RestHelper";

export class UploadHelper {
    private uploadInput: RefObject<HTMLInputElement>;
    private restHelper = new RestHelper();

    constructor(uploadInput: RefObject<HTMLInputElement>) {
        this.uploadInput = uploadInput;
    }

    handleUpload(e: import("react").MouseEvent<HTMLButtonElement, MouseEvent>): Promise<RestErrors | string> {
        e.preventDefault();

        if(!this.uploadInput.current || !this.uploadInput.current.files || this.uploadInput.current.files.length === 0) {
            return Promise.reject(RestErrors.MissingPayload);
        }

        let file = this.uploadInput.current.files[0];
        let formData = new FormData();
        formData.append('file', file);

        return this.restHelper.restHandler(formData, RestMethods.POST, "/api/v1/image");
    }
}