import { Component, Input, OnInit } from "@angular/core";
import {
    IonToast,
  } from '@ionic/angular/standalone';
import { MessageAlertToastService } from "./message-alert-toast.service";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";

@Component({
    selector:'message-alert-toast',
    templateUrl:'./message-alert-toast.component.html',
    styleUrls:['./message-alert-toast.component.scss'],
    imports:[
        CommonModule,
        FormsModule,
        IonToast
    ]
})

export class MessageAlertComponent implements OnInit{
    @Input()
    set message(value:string){
        this.messageToast = value;
    }

    messageToast=""
    isToastOpen = false;

    constructor(private messageAlertToastService:MessageAlertToastService){}

    ngOnInit(): void {
        this.messageAlertToastService.toastIsOpen.subscribe(status =>{
            this.isToastOpen = status;
        })
    }

    setOpen(isOpen: boolean) {
        this.isToastOpen = isOpen;
    }

}