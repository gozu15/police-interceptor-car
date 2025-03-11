import { Injectable } from "@angular/core";
import { environment } from "../../../environments/environment.prod";
import { FactoryApi } from "../../shared/controls/factory-api.controls";
import { Observable } from "rxjs";
import { AuthenticationCredential } from "./models/authentication.model";
import { AuthenticationResponse } from "./models/auth-response.model";

@Injectable({
    providedIn:'root'
})

export class AuthenticationApiService{
    private urlApi = environment.apiUrl
    private route = `${this.urlApi}auth`

    constructor(private factoryApi:FactoryApi){}

    logIn(credentials:AuthenticationCredential):Observable<AuthenticationResponse>{
        return this.factoryApi.post<AuthenticationResponse,AuthenticationCredential>(this.route,credentials)
    }
}