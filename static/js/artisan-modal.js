/**
 * HULEGEB STATIC SITE - ARTISAN STORY MODAL
 * Modal with artisan profile and certificate download
 */

class ArtisanModal {
  constructor() {
    this.modal = null;
    this.openBtn = null;
    this.closeBtn = null;
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
    this.modal = document.querySelector('#artisan-modal');
    this.openBtn = document.querySelector('[data-open-artisan-modal]');
    this.closeBtn = document.querySelector('[data-close-artisan-modal]');

    if (!this.modal) return;

    // Open modal
    if (this.openBtn) {
      this.openBtn.addEventListener('click', () => this.open());
    }

    // Close modal
    if (this.closeBtn) {
      this.closeBtn.addEventListener('click', () => this.close());
    }

    // Close on overlay click
    this.modal.addEventListener('click', (e) => {
      if (e.target === this.modal) {
        this.close();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.modal.classList.contains('active')) {
        this.close();
      }
    });
  }

  open() {
    this.modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Focus trap
    const focusableElements = this.modal.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    if (focusableElements.length > 0) {
      focusableElements[0].focus();
    }
  }

  close() {
    this.modal.classList.remove('active');
    document.body.style.overflow = '';

    // Return focus to trigger
    if (this.openBtn) {
      this.openBtn.focus();
    }
  }
}

// Initialize
new ArtisanModal();
