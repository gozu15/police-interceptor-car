import { Component, OnInit } from '@angular/core';
import { LoadingStateService } from './loading.state.service';
import {
  LoadingBarModule, 
  LoadingBarService, 
  NgxLoadingBar
} from '@ngx-loading-bar/core';

@Component({
  selector: 'app-loading',
  templateUrl: './loading.component.html',
  styleUrls: ['./loading.component.scss'],
  standalone:true,
  imports:[NgxLoadingBar,]
})
export class LoadingComponent  implements OnInit {
  loader
  constructor(private loadingService:LoadingStateService,private loadingBarService:LoadingBarService) { 
    this.loader = this.loadingBarService.useRef();
  }

  ngOnInit() {
  
    this.loadingService.loading
    .subscribe(status => {
      if(status){
        this.showLoadingComponent()
      }else{
        this.closeLoadingComponent()
      }
    })
  }

  showLoadingComponent(){   
    this.loader.start();
  }

  closeLoadingComponent(){
    if(this.loader){
      this.loader.complete();
    }
  }

}
