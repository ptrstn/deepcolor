import { RestErrors, RestHelper, RestMethods } from "./RestHelper";

export class UploadPayload {
    private constructor() {}

    public id: number | undefined;
    public original: string | undefined;
    public colored: string | undefined;
}

export class ModelsInfo {
    private constructor() {}

    public models: { name: string; var: string; }[] | undefined;
}

export class UploadHelper {
    private restHelper = new RestHelper();

    handleUpload(files: FileList | undefined | null, model: string): Promise<RestErrors | UploadPayload> {
        if(files === undefined || files === null || files.length === 0) {
            return Promise.reject(RestErrors.MissingPayload);
        }

        let file = files[0];
        let formData = new FormData();
        formData.append('file', file);
        formData.append('model', model);

        return this.restHelper.restHandler(RestMethods.POST, "/api/v1/images/", formData);
    }

    getModels(): Promise<RestErrors | ModelsInfo> {
        return this.restHelper.restHandler(RestMethods.POST, "/api/v1/models/");
    }
}