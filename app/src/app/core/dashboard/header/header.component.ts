import {
  Component,
  Output,
  EventEmitter,
  Input,
  ViewEncapsulation,
} from '@angular/core';
import { TablerIconComponent,provideTablerIcons } from 'angular-tabler-icons';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { NgScrollbarModule } from 'ngx-scrollbar';
import { MaterialModule } from '../../../material.module';
import { IconMenu2, IconNumber18Small, IconBell, IconUser, IconMail, IconListCheck } from "angular-tabler-icons/icons";


@Component({
  selector: 'app-header',
  imports: [
    RouterModule,
    CommonModule,
    NgScrollbarModule,
    TablerIconComponent,
    MaterialModule,
  ],
  providers:[
    provideTablerIcons({
      IconMenu2,
      IconNumber18Small,
      IconBell,
      IconUser,
      IconMail,
      IconListCheck
    })
  ],
  templateUrl: './header.component.html',
  encapsulation: ViewEncapsulation.None,
})
export class HeaderComponent {
  @Input() showToggle = true;
  @Input() toggleChecked = false;
  @Output() toggleMobileNav = new EventEmitter<void>();
}