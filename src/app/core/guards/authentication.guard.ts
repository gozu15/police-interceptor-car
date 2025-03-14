import { Injectable } from "@angular/core";
import { ActivatedRouteSnapshot, CanActivate, GuardResult, MaybeAsync, Router, RouterStateSnapshot } from "@angular/router";
import { AuthenticationStateService } from "../authentication/authentication.state.service";

@Injectable({
    providedIn:'root'
})

export class AuthenticationGuard implements CanActivate{
    
    constructor(private authenticationStateService:AuthenticationStateService, private router:Router){}
    
    canActivate(): boolean {
        const verifyUserIsLogged = this.authenticationStateService.userIsLogged()
        if(!verifyUserIsLogged){
            this.router.navigate(['/authentication'])
            return false
        }
        return true
    }

}