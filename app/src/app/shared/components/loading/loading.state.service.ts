import { Injectable } from "@angular/core";
import { LoadingBarService } from "@ngx-loading-bar/core";
import { BehaviorSubject } from "rxjs";

@Injectable({
    providedIn:'root'
})

export class LoadingStateService{
    private loadingState:BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false)

    get loading(){
        return this.loadingState.asObservable()
    }

    startLoading(){
        this.loadingState.next(true);
    }

    closeLoading(){
        this.loadingState.next(false)
    }
}