import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { PRODUCTS } from '../../data/products';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-details',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './product-details.html',
  styleUrls: ['./product-details.css']
})
export class ProductDetailsComponent {
  product: Product | undefined;

  constructor(route: ActivatedRoute) {
    const id = Number(route.snapshot.paramMap.get('id'));
    this.product = PRODUCTS.find(p => p.id === id);
  }
}
