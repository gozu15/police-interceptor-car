import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path:'authentication',
        loadComponent:() => import('./core/authentication/authentication.component').then(m => m.AuthenticationComponent)
    },
    {
        path:'main',
        loadComponent:() => import('./core/authentication/authentication.component').then(m => m.AuthenticationComponent)
    }
];
