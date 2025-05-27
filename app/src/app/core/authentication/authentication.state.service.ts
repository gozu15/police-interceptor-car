import { Injectable } from "@angular/core";
import { AuthenticationApiService } from "./authentication.api.service";
import { AuthenticationCredential } from "./models/authentication.model";
import { LoadingStateService } from "../../shared/components/loading/loading.state.service";
import { LocalstorageService } from "../../services/localstorage.service";
import { TOKEN } from "../../shared/constants/authentication.constant";
import { AuthenticationResponse } from "./models/auth-response.model";

@Injectable({
    providedIn:'root'
})

export class AuthenticationStateService{
    
    constructor(private authenticationApiService:AuthenticationApiService, 
                private loadingStateService:LoadingStateService,
                private localstorageService:LocalstorageService){

    }

    logIn(userCredentials:AuthenticationCredential){
        this.loadingStateService.startLoading()
        this.authenticationApiService.logIn(userCredentials).subscribe({
            next:response => {
                this.loadingStateService.closeLoading()
                console.log("respionse",response)
            },
            error:error => {
                this.loadingStateService.closeLoading()
                console.log("error",error)
            }
        })
    }

    userIsLogged():boolean{
        const respUserLogged = this.localstorageService.getLocalstorage<AuthenticationResponse>(TOKEN)
        return respUserLogged !== null ? true  : false;
    }
}