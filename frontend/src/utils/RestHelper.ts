export enum RestMethods {
    GET = "GET",
    PUT = "PUT",
    PATCH = "PATCH",
    POST = "POST",
    DELETE = "DELETE"
}

export enum RestErrors {
    MissingPayload,
    MalformedJson,
    BackendUnavailable
}

export class RestHelper {
    public restHandler(method: RestMethods, path: string, payload?: any): Promise<RestErrors | any> {
        return new Promise(
            (resolve, reject) => {
                let request = new XMLHttpRequest();
                request.open(method, path);
                request.addEventListener('load', () => {
                    if (request.status >= 200 && request.status < 300) {
                        try {
                            var data = JSON.parse(request.response);
                            resolve(data);
                        } catch(e) {
                            reject(RestErrors.MalformedJson)
                        }
                    } else {
                        reject(RestErrors.BackendUnavailable);
                        console.warn(request.statusText)
                    }
                });
                request.send(payload);
        });
    }
}