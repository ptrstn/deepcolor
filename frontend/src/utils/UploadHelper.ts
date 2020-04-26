import { RestErrors, RestHelper, RestMethods } from "./RestHelper";

export class UploadPayload {
    private constructor() {}

    public id: number | undefined;
    public original: string | undefined;
    public colored: string | undefined;
}

export class UploadHelper {
    private restHelper = new RestHelper();

    handleUpload(files: FileList | undefined | null): Promise<RestErrors | UploadPayload> {
        if(files === undefined || files === null || files.length === 0) {
            return Promise.reject(RestErrors.MissingPayload);
        }

        let file = files[0];
        let formData = new FormData();
        formData.append('file', file);

        return this.restHelper.restHandler(formData, RestMethods.POST, "/api/v1/images/");
    }
}