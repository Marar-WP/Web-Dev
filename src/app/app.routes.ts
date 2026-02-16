import { Routes } from '@angular/router';
import { ProductListComponent } from './components/product-list/product-list';
import { AboutComponent } from './pages/about/about';
import { ProductDetailsComponent } from './pages/product-details/product-details';

export const routes: Routes = [
  { path: '', component: ProductListComponent },
  { path: 'about', component: AboutComponent },
  { path: 'products/:id', component: ProductDetailsComponent },
  { path: '**', redirectTo: '' }
];
