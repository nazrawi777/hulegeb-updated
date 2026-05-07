/**
 * HULEGEB STATIC SITE - PRODUCT VARIANTS
 * Handles variant switching, image gallery, and deep linking
 */

class ProductPage {
  constructor() {
    this.product = null;
    this.currentVariant = null;
    this.currentImageIndex = 0;
    this.touchStartX = 0;
    this.touchEndX = 0;

    this.init();
  }

  init() {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => this.setup());
    } else {
      this.setup();
    }
  }

  setup() {
    // Get product slug from data attribute or URL
    const productSlug = document.body.dataset.productSlug;
    if (!productSlug) return;

    this.product = window.getProductBySlug(productSlug);
    if (!this.product) return;

    // Get variant from URL or use default
    const urlParams = new URLSearchParams(window.location.search);
    const variantSlug = urlParams.get('variant') || this.product.default_variant;
    
    this.currentVariant = window.getVariantBySlug(this.product, variantSlug) || 
                          window.getVariantBySlug(this.product, this.product.default_variant);

    this.bindEvents();
    this.updateDisplay();
  }

  bindEvents() {
    // Variant swatches
    document.querySelectorAll('.variant-swatch').forEach(swatch => {
      swatch.addEventListener('click', (e) => {
        const variantSlug = e.currentTarget.dataset.variant;
        this.selectVariant(variantSlug);
      });
    });

    // Gallery thumbnails
    document.querySelectorAll('.gallery-thumb').forEach((thumb, index) => {
      thumb.addEventListener('click', () => {
        this.selectImage(index);
      });
    });

    // Gallery navigation
    const prevBtn = document.querySelector('.gallery-nav.prev');
    const nextBtn = document.querySelector('.gallery-nav.next');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => this.prevImage());
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', () => this.nextImage());
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') this.prevImage();
      if (e.key === 'ArrowRight') this.nextImage();
    });

    // Touch/swipe support
    const gallery = document.querySelector('.gallery-main');
    if (gallery) {
      gallery.addEventListener('touchstart', (e) => {
        this.touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      gallery.addEventListener('touchend', (e) => {
        this.touchEndX = e.changedTouches[0].screenX;
        this.handleSwipe();
      }, { passive: true });
    }

    // Tabs
    document.querySelectorAll('.tab-button').forEach(tab => {
      tab.addEventListener('click', (e) => {
        const tabId = e.currentTarget.dataset.tab;
        this.selectTab(tabId);
      });
    });

    // Quantity buttons (display only)
    const qtyMinus = document.querySelector('.qty-minus');
    const qtyPlus = document.querySelector('.qty-plus');
    const qtyValue = document.querySelector('.quantity-value');

    if (qtyMinus && qtyPlus && qtyValue) {
      let qty = 1;
      qtyMinus.addEventListener('click', () => {
        if (qty > 1) {
          qty--;
          qtyValue.textContent = qty;
        }
      });
      qtyPlus.addEventListener('click', () => {
        const maxQty = this.currentVariant?.inventory || 99;
        if (qty < maxQty) {
          qty++;
          qtyValue.textContent = qty;
        }
      });
    }
  }

  selectVariant(variantSlug) {
    const variant = window.getVariantBySlug(this.product, variantSlug);
    if (!variant) return;

    this.currentVariant = variant;
    this.currentImageIndex = 0;

    // Update URL without reload
    const url = new URL(window.location);
    url.searchParams.set('variant', variantSlug);
    window.history.pushState({}, '', url);

    this.updateDisplay();
  }

  updateDisplay() {
    // Update price
    const priceElement = document.querySelector('.price-current');
    if (priceElement) {
      priceElement.textContent = window.formatPrice(this.currentVariant.price, this.product.currency);
    }

    // Update swatches active state
    document.querySelectorAll('.variant-swatch').forEach(swatch => {
      swatch.classList.remove('active');
      if (swatch.dataset.variant === this.currentVariant.slug) {
        swatch.classList.add('active');
      }
    });

    // Update variant label
    const variantLabel = document.querySelector('.variants-label span');
    if (variantLabel) {
      variantLabel.textContent = this.currentVariant.name;
    }

    // Update inventory status
    const inventoryStatus = document.querySelector('.inventory-status');
    if (inventoryStatus) {
      const inv = this.currentVariant.inventory;
      if (inv > 10) {
        inventoryStatus.textContent = 'In Stock';
        inventoryStatus.className = 'inventory-status in-stock';
      } else if (inv > 0) {
        inventoryStatus.textContent = `Only ${inv} left`;
        inventoryStatus.className = 'inventory-status low-stock';
      } else {
        inventoryStatus.textContent = 'Out of Stock';
        inventoryStatus.className = 'inventory-status';
      }
    }

    // Update main image with fade
    this.updateMainImage();

    // Update thumbnails
    this.updateThumbnails();
  }

  updateMainImage() {
    const mainImage = document.querySelector('.gallery-main-image');
    if (!mainImage) return;

    // Add fade out
    mainImage.classList.add('fade-out');

    setTimeout(() => {
      // Update image src
      const imageSrc = this.getVariantImage(this.currentImageIndex);
      mainImage.src = imageSrc;
      mainImage.alt = `${this.product.brand} ${this.product.title} — ${this.currentVariant.name} — ${this.currentVariant.images[this.currentImageIndex] || 'front'} view`;
      
      // Remove fade
      mainImage.classList.remove('fade-out');
    }, 150);
  }

  updateThumbnails() {
    const thumbs = document.querySelectorAll('.gallery-thumb');
    thumbs.forEach((thumb, index) => {
      thumb.classList.remove('active');
      if (index === this.currentImageIndex) {
        thumb.classList.add('active');
      }

      // Update thumbnail image
      const img = thumb.querySelector('img');
      if (img) {
        const imageSrc = this.getVariantImage(index);
        img.src = imageSrc;
      }
    });
  }

  getVariantImage(index) {
    // In a real implementation, this would return different images per variant
    // For now, return the product's main image
    return window.getProductImage(this.product.slug);
  }

  selectImage(index) {
    if (index < 0 || index >= this.currentVariant.images.length) return;
    this.currentImageIndex = index;
    this.updateMainImage();
    this.updateThumbnails();
  }

  prevImage() {
    const newIndex = this.currentImageIndex - 1;
    if (newIndex >= 0) {
      this.selectImage(newIndex);
    } else {
      this.selectImage(this.currentVariant.images.length - 1);
    }
  }

  nextImage() {
    const newIndex = this.currentImageIndex + 1;
    if (newIndex < this.currentVariant.images.length) {
      this.selectImage(newIndex);
    } else {
      this.selectImage(0);
    }
  }

  handleSwipe() {
    const threshold = 50;
    const diff = this.touchStartX - this.touchEndX;

    if (Math.abs(diff) > threshold) {
      if (diff > 0) {
        this.nextImage();
      } else {
        this.prevImage();
      }
    }
  }

  selectTab(tabId) {
    // Update tab buttons
    document.querySelectorAll('.tab-button').forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.tab === tabId) {
        btn.classList.add('active');
      }
    });

    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => {
      content.classList.remove('active');
      if (content.id === tabId) {
        content.classList.add('active');
      }
    });
  }
}

// Initialize
new ProductPage();
