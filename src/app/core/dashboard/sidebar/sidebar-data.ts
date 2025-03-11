import { NavItem } from './nav-item/nav-item';

export const navItems: NavItem[] = [
  {
    navCap: 'Home',
  },
  {
    displayName: 'Dashboard',
    iconName: 'layout-grid-add',
    route: '/home/main',
  },
  {
    displayName: 'Interceptor vehiculos',
    iconName: 'aperture',
    route: '/home/police-car-interceptor',
  },
  {
    displayName: 'Vehiculos registrados',
    iconName: 'shopping-cart',
    route: '',
  },
  {
    displayName: 'Efectivos policiales',
    iconName: 'shopping-cart',
    route: '',
    chip: true,
    external: true,
    chipClass: 'bg-secondary text-white',
  }
];
