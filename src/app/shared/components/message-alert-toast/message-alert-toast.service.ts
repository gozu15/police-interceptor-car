import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MessageAlertToastService {

  private _toastIsOpen$ = new BehaviorSubject<boolean>(false)

  get toastIsOpen(){
    return this._toastIsOpen$.asObservable()
  }

  constructor() { }

  openToast(){
    this._toastIsOpen$.next(true)
  }

  closeToast(){
    this._toastIsOpen$.next(false)
  }
}
