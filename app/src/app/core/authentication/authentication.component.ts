import { CommonModule } from "@angular/common";
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from "@angular/forms";
import { Component } from "@angular/core";
import { MaterialModule } from "../../material.module";
import { Router, RouterModule } from "@angular/router";
import { AuthenticationStateService } from "./authentication.state.service";
import { AuthenticationCredential } from "./models/authentication.model";
import { checkInputForm } from "../../shared/tools/form-has-error.tools";

@Component({
    selector:'authentication-app',
    templateUrl:'./authentication.component.html',
    styleUrls:['./authentication.component.scss'],
    standalone:true,
    imports:[RouterModule, MaterialModule, FormsModule, ReactiveFormsModule]
})

export class AuthenticationComponent{
    constructor( private router: Router, private authenticationStateService:AuthenticationStateService) {}

    userCredentialsForm = new FormGroup({
      username: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required, Validators.minLength(8)]),
    });
  
    submit() {
      // console.log(this.form.value);
      this.userCredentialsForm.markAllAsTouched()
      const formValid = this.userCredentialsForm.valid
      if(formValid){
        const credentials:AuthenticationCredential = {
          username:this.userCredentialsForm.getRawValue().username as string,
          password:this.userCredentialsForm.getRawValue().password as string
        }
        this.authenticationStateService.logIn(credentials)
        this.router.navigate(['/']);
      }
    }

    verifyInputHasError(formKey:string, errorCode:string){
      return checkInputForm(this.userCredentialsForm,formKey,errorCode)
    }
  }