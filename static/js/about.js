/**
 * Hulegeb About Us Page - JavaScript
 * 
 * Vanilla JavaScript for animations, counters, and scroll triggers.
 * No build step required - this file is human-editable.
 * 
 * FEATURES:
 * - Scroll-triggered reveal animations using Intersection Observer
 * - Animated counters (0 → target value)
 * - Button micro-interactions
 * - Optional content loading from JSON
 * 
 * EDITING GUIDE:
 * - Animation thresholds: Adjust IntersectionObserver options
 * - Counter duration: Modify the `duration` parameter in animateCounter()
 * - Add new reveal elements: Use classes like 'reveal-on-scroll', 'timeline-item'
 */

(function() {
  'use strict';

  // ============================================
  // UTILITY FUNCTIONS
  // ============================================
  
  /**
   * Debounce function for performance optimization
   * @param {Function} func - Function to debounce
   * @param {number} wait - Wait time in ms
   * @returns {Function}
   */
  function debounce(func, wait = 100) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }

  /**
   * Easing function for smooth animations
   * @param {number} t - Progress (0-1)
   * @returns {number}
   */
  function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
  }

  // ============================================
  // SCROLL REVEAL ANIMATIONS
  // ============================================
  
  /**
   * Initialize scroll-triggered reveal animations
   * Uses Intersection Observer for performance
   */
  function initScrollReveal() {
    const revealElements = document.querySelectorAll(
      '.reveal-on-scroll, .reveal-slide-left, .reveal-slide-right, .timeline-item'
    );

    if (!revealElements.length) return;

    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach(el => revealObserver.observe(el));
  }

  // ============================================
  // COUNTER ANIMATIONS
  // ============================================
  
  /**
   * Animate a counter from 0 to target value
   * @param {HTMLElement} element - Counter element
   * @param {number} target - Target value
   * @param {string} suffix - Suffix to append (e.g., '+', '%')
   * @param {number} duration - Animation duration in ms
   */
  function animateCounter(element, target, suffix = '', duration = 2000) {
    const startTime = performance.now();
    const startValue = 0;

    function updateCounter(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutQuart(progress);
      const currentValue = Math.round(startValue + (target - startValue) * easedProgress);

      element.textContent = currentValue.toLocaleString() + suffix;

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        // Add a subtle pop animation when complete
        element.style.animation = 'counter-pop 0.3s ease-out';
      }
    }

    requestAnimationFrame(updateCounter);
  }

  /**
   * Initialize all counter animations
   * Triggers when counters come into view
   */
  function initCounters() {
    const counterElements = document.querySelectorAll('.counter-number[data-target]');

    if (!counterElements.length) return;

    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.dataset.target, 10);
          const suffix = el.dataset.suffix || '';
          
          animateCounter(el, target, suffix);
          counterObserver.unobserve(el);
        }
      });
    }, { threshold: 0.3 });

    counterElements.forEach(el => counterObserver.observe(el));
  }

  // ============================================
  // BUTTON MICRO-INTERACTIONS
  // ============================================
  
  /**
   * Initialize button click animations
   */
  function initButtonInteractions() {
    const donateBtn = document.getElementById('donate-btn');
    const volunteerBtn = document.getElementById('volunteer-btn');

    function handleButtonClick(e) {
      const btn = e.currentTarget;
      btn.style.transform = 'translateY(0) scale(0.95)';
      
      // Find heart icon and fill it on donate button
      if (btn.id === 'donate-btn') {
        const heartIcon = btn.querySelector('svg');
        if (heartIcon) {
          heartIcon.style.fill = 'currentColor';
        }
      }
      
      setTimeout(() => {
        btn.style.transform = '';
        if (btn.id === 'donate-btn') {
          const heartIcon = btn.querySelector('svg');
          if (heartIcon) {
            heartIcon.style.fill = 'none';
          }
        }
      }, 150);
    }

    if (donateBtn) {
      donateBtn.addEventListener('click', handleButtonClick);
    }
    
    if (volunteerBtn) {
      volunteerBtn.addEventListener('click', handleButtonClick);
    }
  }

  // ============================================
  // SMOOTH SCROLL FOR ANCHOR LINKS
  // ============================================
  
  /**
   * Initialize smooth scrolling for internal links
   */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }

  // ============================================
  // CONTENT LOADING FROM JSON (OPTIONAL)
  // ============================================
  
  /**
   * Load content from JSON file and update DOM
   * This allows editing content without touching HTML
   * @param {string} url - URL to JSON file
   */
  async function loadContentFromJSON(url = '../content/about.json') {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        console.log('Using static HTML content (JSON not loaded)');
        return;
      }
      
      const content = await response.json();
      updateDOMWithContent(content);
      
    } catch (error) {
      console.log('Using static HTML content:', error.message);
    }
  }

  /**
   * Update DOM elements with content from JSON
   * Elements use data-content attribute to specify JSON path
   * @param {Object} content - Content object from JSON
   */
  function updateDOMWithContent(content) {
    const elements = document.querySelectorAll('[data-content]');
    
    elements.forEach(el => {
      const path = el.dataset.content;
      const value = getNestedValue(content, path);
      
      if (value !== undefined) {
        el.textContent = value;
      }
    });

    // Update SEO meta tags
    if (content.seo) {
      document.title = content.seo.title;
      
      const metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc) {
        metaDesc.setAttribute('content', content.seo.description);
      }
      
      const ogTitle = document.querySelector('meta[property="og:title"]');
      if (ogTitle) {
        ogTitle.setAttribute('content', content.seo.title);
      }
      
      const ogDesc = document.querySelector('meta[property="og:description"]');
      if (ogDesc) {
        ogDesc.setAttribute('content', content.seo.description);
      }
    }
  }

  /**
   * Get nested value from object using dot notation
   * @param {Object} obj - Source object
   * @param {string} path - Dot-notation path (e.g., 'organization.name')
   * @returns {*}
   */
  function getNestedValue(obj, path) {
    return path.split('.').reduce((current, key) => {
      return current && current[key] !== undefined ? current[key] : undefined;
    }, obj);
  }

  // ============================================
  // LUCIDE ICONS INITIALIZATION
  // ============================================
  
  /**
   * Initialize Lucide icons
   */
  function initLucideIcons() {
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  // ============================================
  // INITIALIZATION
  // ============================================
  
  /**
   * Main initialization function
   * Called when DOM is ready
   */
  function init() {
    // Initialize Lucide icons first
    initLucideIcons();
    
    // Initialize animations and interactions
    initScrollReveal();
    initCounters();
    initButtonInteractions();
    initSmoothScroll();
    
    // Optionally load content from JSON
    // Uncomment the line below to enable JSON content loading:
    // loadContentFromJSON('../content/about.json');
    
    console.log('Hulegeb About Us page initialized');
  }

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // ============================================
  // EXPORTS FOR DEBUGGING (optional)
  // ============================================
  window.HulegepAbout = {
    initScrollReveal,
    initCounters,
    animateCounter,
    loadContentFromJSON
  };

})();
