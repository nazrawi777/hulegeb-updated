/**
 * ==========================================================================
 * HULEGEB SERVICES PAGE - STATIC HTML JAVASCRIPT
 * Hand-coded vanilla JavaScript
 * Features: Scroll reveal, accordion, form validation, floating CTA
 * ==========================================================================
 */

(function() {
  'use strict';

  /* ==========================================================================
     REDUCED MOTION CHECK
     EDIT: Respects user's motion preferences
     ========================================================================== */
  
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ==========================================================================
     SCROLL REVEAL
     EDIT: Reusable IntersectionObserver for reveal animations
     ========================================================================== */

  function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal-on-scroll');

    // If user prefers reduced motion, reveal all immediately
    if (prefersReducedMotion) {
      revealElements.forEach(function(el) {
        el.classList.add('revealed');
      });
      return;
    }

    // Create IntersectionObserver
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Observe all reveal elements
    revealElements.forEach(function(el) {
      observer.observe(el);
    });
  }

  /* ==========================================================================
     ACCORDION
     EDIT: Simple accordion toggle for Training Approach sections
     ========================================================================== */

  function initAccordions() {
    const accordionTriggers = document.querySelectorAll('.accordion__trigger');

    accordionTriggers.forEach(function(trigger) {
      trigger.addEventListener('click', function() {
        const item = this.closest('.accordion__item');
        const isOpen = item.getAttribute('data-state') === 'open';
        
        // Toggle state
        item.setAttribute('data-state', isOpen ? 'closed' : 'open');
        this.setAttribute('aria-expanded', !isOpen);
      });

      // Keyboard accessibility - Enter and Space
      trigger.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.click();
        }
      });
    });
  }

  /* ==========================================================================
     FORM VALIDATION
     EDIT: Client-side validation with accessible error messages
     ========================================================================== */

  function initFormValidation() {
    const form = document.getElementById('contact-form');
    
    if (!form) return;

    form.addEventListener('submit', function(e) {
      e.preventDefault();
      
      let isValid = true;
      const errors = {};

      // Get form fields
      const nameInput = document.getElementById('name');
      const emailInput = document.getElementById('email');
      const messageInput = document.getElementById('message');

      // Get error elements
      const nameError = document.getElementById('name-error');
      const emailError = document.getElementById('email-error');
      const messageError = document.getElementById('message-error');

      // Clear previous errors
      clearErrors();

      // Validate name
      if (!nameInput.value.trim()) {
        errors.name = 'Please enter your name';
        isValid = false;
      }

      // Validate email
      if (!emailInput.value.trim()) {
        errors.email = 'Please enter your email';
        isValid = false;
      } else if (!isValidEmail(emailInput.value)) {
        errors.email = 'Please enter a valid email address';
        isValid = false;
      }

      // Validate message
      if (!messageInput.value.trim()) {
        errors.message = 'Please enter your message';
        isValid = false;
      }

      // Show errors or submit
      if (!isValid) {
        if (errors.name) {
          showError(nameInput, nameError, errors.name);
        }
        if (errors.email) {
          showError(emailInput, emailError, errors.email);
        }
        if (errors.message) {
          showError(messageInput, messageError, errors.message);
        }
      } else {
        // EDIT: Handle successful form submission
        alert('Thank you for your message! We will get back to you soon.');
        form.reset();
      }
    });

    function isValidEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    function showError(input, errorEl, message) {
      input.classList.add('error');
      input.setAttribute('aria-invalid', 'true');
      errorEl.textContent = message;
      errorEl.classList.add('visible');
    }

    function clearErrors() {
      const inputs = form.querySelectorAll('.form-input, .form-textarea');
      const errorMessages = form.querySelectorAll('.form-error');
      
      inputs.forEach(function(input) {
        input.classList.remove('error');
        input.setAttribute('aria-invalid', 'false');
      });
      
      errorMessages.forEach(function(error) {
        error.classList.remove('visible');
        error.textContent = '';
      });
    }
  }

  /* ==========================================================================
     FLOATING CTA
     EDIT: Smooth scroll to contact section
     ========================================================================== */

  function initFloatingCTA() {
    const floatingCTA = document.querySelector('.floating-cta');
    
    if (!floatingCTA) return;

    floatingCTA.addEventListener('click', function() {
      const contactSection = document.getElementById('contact');
      
      if (contactSection) {
        // Use smooth scroll if not reduced motion
        if (prefersReducedMotion) {
          contactSection.scrollIntoView();
        } else {
          contactSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }

  /* ==========================================================================
     SMOOTH SCROLL FOR ANCHOR LINKS
     ========================================================================== */

  function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    anchorLinks.forEach(function(link) {
      link.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        
        if (href === '#') return;
        
        const target = document.querySelector(href);
        
        if (target) {
          e.preventDefault();
          
          if (prefersReducedMotion) {
            target.scrollIntoView();
          } else {
            target.scrollIntoView({ behavior: 'smooth' });
          }
        }
      });
    });
  }

  /* ==========================================================================
     INITIALIZE ALL
     ========================================================================== */

  function init() {
    initScrollReveal();
    initAccordions();
    initFormValidation();
    initFloatingCTA();
    initSmoothScroll();
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
