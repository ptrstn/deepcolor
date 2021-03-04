import { RestErrors, RestHelper, RestMethods } from "./RestHelper";

export class UploadPayload {
    private constructor() {}

    public id: number | undefined;
    public original: string | undefined;
    public colored: string | undefined;
}

export class ModelsInfo {
    private constructor() {}

    public strategies: { name: string; var: string; }[] | undefined;
}

export class UploadHelper {
    private restHelper = new RestHelper();

    handleUpload(files: FileList | undefined | null, strategy: string): Promise<RestErrors | UploadPayload> {
        if(files === undefined || files === null || files.length === 0) {
            return Promise.reject(RestErrors.MissingPayload);
        }

        let file = files[0];
        let formData = new FormData();
        formData.append('file', file);
        formData.append('strategy', strategy);

        return this.restHelper.restHandler(RestMethods.POST, process.env.PUBLIC_URL + "/api/v1/images/", formData);
    }

    getModels(): Promise<RestErrors | ModelsInfo> {
        return this.restHelper.restHandler(RestMethods.GET, process.env.PUBLIC_URL + "/api/v1/strategies/");
    }
}