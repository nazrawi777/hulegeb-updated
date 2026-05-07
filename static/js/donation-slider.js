/**
 * HULEGEB STATIC SITE - DONATION SLIDER
 * UI-only donation slider that updates impact display
 */

class DonationSlider {
  constructor() {
    this.slider = null;
    this.amountDisplay = null;
    this.impactDisplay = null;
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
    this.slider = document.querySelector('.donation-slider');
    this.amountDisplay = document.querySelector('.donation-amount');
    this.impactDisplay = document.querySelector('.donation-impact');

    if (!this.slider) return;

    this.slider.addEventListener('input', (e) => {
      this.updateDisplay(parseInt(e.target.value, 10));
    });

    // Set initial value
    this.updateDisplay(parseInt(this.slider.value, 10));
  }

  updateDisplay(amount) {
    if (this.amountDisplay) {
      this.amountDisplay.textContent = `${amount} ETB`;
    }

    if (this.impactDisplay) {
      this.impactDisplay.textContent = this.calculateImpact(amount);
    }
  }

  calculateImpact(amount) {
    if (amount === 0) {
      return "Select an amount to see your impact";
    } else if (amount <= 5) {
      return "Provides 1 hour of vocational training materials";
    } else if (amount <= 10) {
      return "Funds 2 hours of skills training for one artisan";
    } else {
      return "Covers a full day of advanced training workshop";
    }
  }
}

// Initialize
new DonationSlider();
