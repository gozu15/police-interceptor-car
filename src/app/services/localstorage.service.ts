import { Injectable } from "@angular/core";

@Injectable({
    providedIn:'root'
})

export class LocalstorageService{
    getLocalstorage<T>(key:string):T|null{
        const dataStorage = localStorage.getItem(key)
        const data = JSON.parse( dataStorage!== null ? dataStorage : "{}")
        return Object.keys(data).length >0 ? data as T : null
    }

    setLocalstorage<T>(data:T,key:string){
        const convertObjectString = JSON.stringify(data)
        localStorage.setItem(key,convertObjectString)
    }
}