import { CommonModule } from "@angular/common";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { Component } from "@angular/core";

@Component({
    selector:'authentication-app',
    templateUrl:'./authentication.component.html',
    styleUrls:['./authentication.component.scss'],
    standalone:true,
    imports:[CommonModule, FormsModule, ReactiveFormsModule]
})

export class AuthenticationComponent{

}