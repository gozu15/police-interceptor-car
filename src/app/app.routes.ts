import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path:'authentication',
        loadComponent:() => import('./core/authentication/authentication.component').then(m => m.AuthenticationComponent)
    },
    {
        path:'home',
        loadChildren:() => import('./core/core.routes').then(m => m.coreRoute)
    },
    {
        path:'',
        redirectTo:'authentication',
        pathMatch:'full'
    }
];
