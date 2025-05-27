import { Injectable } from "@angular/core";
import {  CanActivate, Router } from "@angular/router";
import { AuthenticationStateService } from "../authentication/authentication.state.service";

@Injectable({
    providedIn:'root'
})

export class MainGuard implements CanActivate{
    
    constructor(private authenticationStateService:AuthenticationStateService, private router:Router){}
    
    canActivate(): boolean {
        const verifyUserIsLogged = this.authenticationStateService.userIsLogged()
        if(verifyUserIsLogged){
            this.router.navigate(['/home'])
            return false
        }
        return true
    }

}