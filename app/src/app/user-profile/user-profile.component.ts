import { CommonModule } from "@angular/common";
import { Component, OnInit, Output } from "@angular/core";
import { UserProfile } from "./models/user-profile.model";

@Component({
    selector:'',
    templateUrl:'./user-profile.component.html',
    styleUrl:'./user-profile.component.scss',
    imports:[CommonModule]
})

export class UserProfileComponent implements OnInit{
    userDataProfile!:UserProfile


    @Output()
    set userData(user:UserProfile){
        this.userDataProfile = user
    }

     

    ngOnInit() {
        
    }
}