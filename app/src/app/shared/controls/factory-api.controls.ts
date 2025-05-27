import { Observable } from "rxjs";
import { RequestControls } from "./request.controls";
import { HttpClient, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({providedIn:'root'})

export class FactoryApi implements RequestControls{

    constructor(private httpClient:HttpClient){}
    
    get<T>(route:string): Observable<T> {
        return this.httpClient.get<T>(route)
    }
    post<T, U>(route:string,data: U): Observable<T> {
        return this.httpClient.post<T>(route,data)
    }
    put<T, U>(route:string,data: U): Observable<T> {
        return this.httpClient.put<T>(route,data)
    }
    delete<T>(route:string,id: number): Observable<T> {
        const params = new HttpParams()
        .set('id',id)
        return this.httpClient.delete<T>(route,{params})
    }

}