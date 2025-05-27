import { Observable } from "rxjs";

export interface RequestControls{
    get<T>(apiRoute:string):Observable<T>
    post<T,U>(apiRoute:string,data:U):Observable<T>
    put<T,U>(apiRoute:string,data:U):Observable<T>
    delete<T>(apiRoute:string,id:number):Observable<T>
}