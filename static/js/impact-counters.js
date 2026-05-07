/**
 * HULEGEB STATIC SITE - IMPACT COUNTERS
 * Animated counters that trigger on scroll
 */

class ImpactCounters {
  constructor() {
    this.counters = [];
    this.hasAnimated = false;
    this.init();
  }

  init() {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => this.setup());
    } else {
      this.setup();
    }
  }

  setup() {
    this.counters = document.querySelectorAll('[data-counter]');
    
    if (this.counters.length === 0) return;

    // Check for reduced motion preference
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (prefersReducedMotion) {
      // Show final values immediately
      this.counters.forEach(counter => {
        const target = parseInt(counter.dataset.target, 10);
        counter.textContent = target.toLocaleString();
        this.updateProgressBar(counter);
      });
      return;
    }

    // Set up intersection observer
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !this.hasAnimated) {
            this.hasAnimated = true;
            this.animateAll();
          }
        });
      },
      { threshold: 0.3 }
    );

    // Observe the impact section
    const section = document.querySelector('.impact-grid');
    if (section) {
      observer.observe(section);
    }
  }

  animateAll() {
    this.counters.forEach((counter, index) => {
      setTimeout(() => {
        this.animateCounter(counter);
      }, index * 150);
    });
  }

  animateCounter(element) {
    const target = parseInt(element.dataset.target, 10);
    const duration = 2000;
    const start = 0;
    const startTime = performance.now();

    const animate = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      
      // Ease out cubic
      const easeOut = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(start + (target - start) * easeOut);
      
      element.textContent = current.toLocaleString();
      
      if (progress < 1) {
        requestAnimationFrame(animate);
      } else {
        element.textContent = target.toLocaleString();
        this.updateProgressBar(element);
      }
    };

    requestAnimationFrame(animate);
  }

  updateProgressBar(counterElement) {
    const card = counterElement.closest('.impact-card');
    if (!card) return;

    const progressBar = card.querySelector('.impact-progress-bar');
    if (!progressBar) return;

    const target = parseInt(counterElement.dataset.target, 10);
    const max = parseInt(counterElement.dataset.max, 10) || target * 1.2;
    const percentage = Math.min((target / max) * 100, 100);

    setTimeout(() => {
      progressBar.style.width = `${percentage}%`;
    }, 100);
  }
}

// Initialize
new ImpactCounters();
