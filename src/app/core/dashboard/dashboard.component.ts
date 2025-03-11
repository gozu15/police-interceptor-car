import { CommonModule } from "@angular/common";
import { BreakpointObserver, MediaMatcher } from '@angular/cdk/layout';
import { Component, ViewChild } from "@angular/core";
import { RouterModule, Router, NavigationEnd } from "@angular/router";
import { Subscription, filter } from "rxjs";
import { CoreService } from "../../services/core.service";
import { HeaderComponent } from "./header/header.component";
import { AppNavItemComponent } from "./sidebar/nav-item/nav-item.component";
import { navItems } from "./sidebar/sidebar-data";
import { SidebarComponent } from "./sidebar/sidebar.component";
import { MaterialModule } from "../../material.module";
import { NgScrollbarModule } from "ngx-scrollbar";
import { MatSidenav, MatSidenavContent } from "@angular/material/sidenav";

const MOBILE_VIEW = 'screen and (max-width: 768px)';
const TABLET_VIEW = 'screen and (min-width: 769px) and (max-width: 1024px)';

@Component({
    selector:'dashboard-app',
    templateUrl:'./dashboard.component.html',
    imports:[
        RouterModule,
        AppNavItemComponent,
        MaterialModule,
        CommonModule,
        SidebarComponent,
        NgScrollbarModule,
        HeaderComponent        
    ]
})

export class DashboardComponent{
    navItems = navItems;

    @ViewChild('leftsidenav')
    public sidenav!: MatSidenav;
    resView = false;
    @ViewChild('content', { static: true }) content!: MatSidenavContent;
    //get options from service
    options
    private layoutChangesSubscription = Subscription.EMPTY;
    private isMobileScreen = false;
    private isContentWidthFixed = true;
    private isCollapsedWidthFixed = false;
    private htmlElement!: HTMLHtmlElement;
  
    get isOver(): boolean {
      return this.isMobileScreen;
    }
  
  
    constructor(
      private settings: CoreService,
      private router: Router,
      private breakpointObserver: BreakpointObserver,
    ) {
        this.options= this.settings.getOptions();
      this.htmlElement = document.querySelector('html')!;
      this.layoutChangesSubscription = this.breakpointObserver
        .observe([MOBILE_VIEW, TABLET_VIEW])
        .subscribe((state) => {
          // SidenavOpened must be reset true when layout changes
          this.options.sidenavOpened = true;
          this.isMobileScreen = state.breakpoints[MOBILE_VIEW];
          if (this.options.sidenavCollapsed == false) {
            this.options.sidenavCollapsed = state.breakpoints[TABLET_VIEW];
          }
        });
  
      // Initialize project theme with options
  
  
      // This is for scroll to top
      this.router.events
        .pipe(filter((event) => event instanceof NavigationEnd))
        .subscribe((e) => {
          this.content.scrollTo({ top: 0 });
        });
    }
  
    ngOnInit(): void { }
  
    ngOnDestroy() {
      this.layoutChangesSubscription.unsubscribe();
    }
  
    toggleCollapsed() {
      this.isContentWidthFixed = false;
      this.options.sidenavCollapsed = !this.options.sidenavCollapsed;
      this.resetCollapsedState();
    }
  
    resetCollapsedState(timer = 400) {
      setTimeout(() => this.settings.setOptions(this.options), timer);
    }
  
    onSidenavClosedStart() {
      this.isContentWidthFixed = false;
    }
  
    onSidenavOpenedChange(isOpened: boolean) {
      this.isCollapsedWidthFixed = !this.isOver;
      this.options.sidenavOpened = isOpened;
      //this.settings.setOptions(this.options);
    }
}