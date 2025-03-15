import { CommonModule } from "@angular/common";
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from "@angular/forms";
import { Component } from "@angular/core";
import { MaterialModule } from "../../material.module";
import { Router, RouterModule } from "@angular/router";

@Component({
    selector:'authentication-app',
    templateUrl:'./authentication.component.html',
    styleUrls:['./authentication.component.scss'],
    standalone:true,
    imports:[RouterModule, MaterialModule, FormsModule, ReactiveFormsModule]
})

export class AuthenticationComponent{
    constructor( private router: Router) {}

    form = new FormGroup({
      uname: new FormControl('', [Validators.required, Validators.minLength(8)]),
      password: new FormControl('', [Validators.required]),
    });
  
    get f() {
      return this.form.controls;
    }
  
    submit() {
      // console.log(this.form.value);
      this.router.navigate(['/']);
    }
}