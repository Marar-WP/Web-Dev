import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-card.html',
  styleUrls: ['./product-card.css']
})
export class ProductCardComponent {

  @Input({ required: true }) product!: Product;

  selectedIndex = 0;

  get stars(): boolean[] {
    const r = Math.round(this.product.rating);
    return Array.from({ length: 5 }, (_, i) => i < r);
  }

  setImage(i: number): void {
    this.selectedIndex = i;
  }

  openKaspi(): void {
    window.open(this.product.link, '_blank', 'noopener,noreferrer');
  }

  get whatsappShareUrl(): string {
    const text = `Check out this product: ${this.product.link}`;
    return `https://wa.me/?text=${encodeURIComponent(text)}`;
  }

  get telegramShareUrl(): string {
    const url = encodeURIComponent(this.product.link);
    const text = encodeURIComponent(this.product.name);
    return `https://t.me/share/url?url=${url}&text=${text}`;
  }
}


