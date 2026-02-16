import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Product } from '../../models/product.model';
import { ProductCardComponent } from '../product-card/product-card';
import { PRODUCTS } from '../../data/products';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule, FormsModule, ProductCardComponent],
  templateUrl: './product-list.html',
  styleUrls: ['./product-list.css']
})
export class ProductListComponent implements OnInit {

  products: Product[] = PRODUCTS;

  searchQuery: string = '';
  filteredProducts: Product[] = [];

  ngOnInit(): void {
    this.filteredProducts = this.products;
  }

  filterProducts(): void {
    const query = this.searchQuery.toLowerCase();

    this.filteredProducts = this.products.filter(product =>
      product.name.toLowerCase().includes(query)
    );
  }

}




