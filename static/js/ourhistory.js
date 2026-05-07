/**
 * Hulegeb About Us Page - JavaScript
 * 
 * This file provides:
 * 1. Scroll-triggered reveal animations
 * 2. Animated counters that start when scrolled into view
 * 3. Accordion functionality for mobile
 * 
 * HOW IT WORKS:
 * - Uses IntersectionObserver for efficient scroll detection
 * - Counters animate using requestAnimationFrame for smooth performance
 * - All animations are GPU-friendly (opacity and transform only)
 * 
 * HOW TO EDIT:
 * - Change counter targets: Edit data-target attribute in HTML
 * - Adjust animation timing: Modify duration constants below
 * - Add new sections: Add .scroll-animate class to any element
 */

(function() {
    'use strict';

    // ========================================
    // CONFIGURATION
    // ========================================
    const CONFIG = {
        // Counter animation duration in milliseconds
        counterDuration: 2000,
        
        // Intersection observer threshold (0-1)
        scrollThreshold: 0.1,
        
        // Stagger delay between timeline items (ms)
        timelineStagger: 150
    };

    // ========================================
    // SCROLL REVEAL ANIMATION
    // ========================================
    function initScrollReveal() {
        const elements = document.querySelectorAll('.scroll-animate');
        
        if (!elements.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    // Unobserve after animation (trigger once)
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: CONFIG.scrollThreshold,
            rootMargin: '0px'
        });

        elements.forEach((el) => {
            observer.observe(el);
        });
    }

    // ========================================
    // TIMELINE ANIMATION
    // ========================================
    function initTimelineAnimation() {
        const timelineItems = document.querySelectorAll('.timeline-item');
        
        if (!timelineItems.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Add staggered delay
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, index * CONFIG.timelineStagger);
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.2,
            rootMargin: '0px'
        });

        timelineItems.forEach((item) => {
            observer.observe(item);
        });
    }

    // ========================================
    // ANIMATED COUNTERS
    // ========================================
    function initCounters() {
        const counters = document.querySelectorAll('.counter-value');
        
        if (!counters.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.3,
            rootMargin: '0px'
        });

        counters.forEach((counter) => {
            observer.observe(counter);
        });
    }

    function animateCounter(element) {
        const target = parseInt(element.dataset.target, 10);
        const suffix = element.dataset.suffix || '';
        const duration = CONFIG.counterDuration;
        const startTime = performance.now();
        const startValue = 0;

        function easeOutQuart(t) {
            return 1 - Math.pow(1 - t, 4);
        }

        function formatNumber(num) {
            return num.toLocaleString();
        }

        function update(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easedProgress = easeOutQuart(progress);
            const currentValue = Math.floor(startValue + (target - startValue) * easedProgress);

            element.textContent = formatNumber(currentValue) + suffix;

            if (progress < 1) {
                requestAnimationFrame(update);
            }
        }

        requestAnimationFrame(update);
    }

    // ========================================
    // ACCORDION
    // ========================================
    function initAccordion() {
        const accordionTriggers = document.querySelectorAll('.accordion-trigger');
        
        if (!accordionTriggers.length) return;

        accordionTriggers.forEach((trigger) => {
            trigger.addEventListener('click', function() {
                const isExpanded = this.getAttribute('aria-expanded') === 'true';
                const contentId = this.getAttribute('aria-controls');
                const content = document.getElementById(contentId);

                if (!content) return;

                // Toggle state
                this.setAttribute('aria-expanded', !isExpanded);
                
                if (isExpanded) {
                    content.classList.remove('expanded');
                } else {
                    content.classList.add('expanded');
                }
            });

            // Keyboard accessibility
            trigger.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    this.click();
                }
            });
        });
    }

    // ========================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ========================================
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;

                const target = document.querySelector(targetId);
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

    // ========================================
    // LOAD CONTENT FROM JSON (Optional)
    // ========================================
    async function loadContentFromJSON() {
        try {
            const response = await fetch('../content/history.json');
            if (!response.ok) {
                console.log('Content JSON not found, using inline content.');
                return null;
            }
            return await response.json();
        } catch (error) {
            console.log('Using inline content (JSON fetch failed):', error.message);
            return null;
        }
    }

    // ========================================
    // INITIALIZATION
    // ========================================
    function init() {
        // Initialize all features when DOM is ready
        initScrollReveal();
        initTimelineAnimation();
        initCounters();
        initAccordion();
        initSmoothScroll();

        // Optional: Load content from JSON
        // Uncomment to enable dynamic content loading
        // loadContentFromJSON().then((data) => {
        //     if (data) {
        //         console.log('Content loaded from JSON:', data);
        //         // You can update DOM elements here based on JSON data
        //     }
        // });

        console.log('Hulegeb About Page initialized');
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
