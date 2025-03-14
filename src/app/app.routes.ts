import { Routes } from '@angular/router';
import { AuthenticationGuard } from './core/guards/authentication.guard';
import { MainGuard } from './core/guards/main.guard';

export const routes: Routes = [
    {
        path:'authentication',
        canActivate:[MainGuard],
        loadComponent:() => import('./core/authentication/authentication.component').then(m => m.AuthenticationComponent)
    },
    {
        path:'home',
        canActivate:[AuthenticationGuard],
        loadChildren:() => import('./core/core.routes').then(m => m.coreRoute)
    },
    {
        path:'',
        redirectTo:'authentication',
        pathMatch:'full'
    }
];
