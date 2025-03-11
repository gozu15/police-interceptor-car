import { CommonModule } from "@angular/common";
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";

@Component({
    selector:'main-app',
    templateUrl:'./main.component.html',
    styleUrls:['./main.component.scss'],
    standalone:true,
    imports:[
        CommonModule,
        FormsModule
    ]
})

export class MainComponent{}