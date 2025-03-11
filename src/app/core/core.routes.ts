import { Routes } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";

export const coreRoute:Routes=[
    {
        path:'',
        component:DashboardComponent,
        children:[
            {
                path:'',
                pathMatch:'full',
                redirectTo:'main'
            },
            {
                path:'main',
                loadComponent:() => import('../main/main.component').then(m => m.MainComponent)
            }
        ]
    }
    
]