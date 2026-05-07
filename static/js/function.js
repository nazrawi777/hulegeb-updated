(function ($) {
    "use strict";

    var $window = $(window);
    var $header = $('header.main-header');

    // Preloader
    $window.on('load', function () {
        $(".preloader").fadeOut(600);
    });

    // Sticky Header on Scroll
    $window.on('scroll', function () {
        if ($window.scrollTop() > 10) {
            $header.addClass('sticky');
        } else {
            $header.removeClass('sticky');
        }
    });



$(document).ready(function () {
    console.log("🚨 MENTOR DIAGNOSTIC: Script started successfully.");

    // 1. Get raw path and clean it (added toLowerCase to kill case-sensitivity)
    var rawPath = window.location.pathname;
    console.log("🚨 RAW PATH from Netlify:", rawPath);

    var currentPage = rawPath.replace(/\/$/, "").replace(".html", "").split("/").pop().toLowerCase();
    
    if (currentPage === "" || currentPage === "index") {
        currentPage = "index";
    }
    console.log("🚨 CLEANED CURRENT PAGE:", currentPage);

    // 2. Loop through links and log the comparison
    $('#menu a.nav-link').each(function () {
        var linkHref = $(this).attr('href');

        if (!linkHref || linkHref === "#") return;

        var linkPage = linkHref.replace(".html", "").toLowerCase();
        
        // This will print every single comparison to your console
        console.log("Comparing link: [" + linkPage + "] with current page: [" + currentPage + "]");

        if (linkPage === currentPage) {
            console.log("✅ MATCH FOUND! Activating:", linkHref);
            $(this).addClass('active');
            $(this).closest('li').addClass('active');
            $(this).parents('.submenu').addClass('active');
        }
    });
});



	
	
	/* Slick Menu JS */
	$('#menu').slicknav({
		label : '',
		prependTo : '.responsive-menu'
	});

	if($("a[href='#top']").length){
		$(document).on("click", "a[href='#top']", function() {
			$("html, body").animate({ scrollTop: 0 }, "slow");
			return false;
		});
	}

	/* Hero Slider Layout JS */
	const hero_slider_layout = new Swiper('.hero-slider-layout .swiper', {
		slidesPerView : 1,
		speed: 1000,
		spaceBetween: 0,
		loop: true,
		autoplay: {
			delay: 4000,
		},
		pagination: {
			el: '.hero-pagination',
			clickable: true,
		},
	});

	/* Testimonial Guarantee Logo Slider JS */
	if ($('.donar-company-slider').length) {
		const donar_company_slider = new Swiper('.donar-company-slider .swiper', {
			slidesPerView : 2,
			speed: 2000,
			spaceBetween: 50,
			loop: true,
			autoplay: {
				delay: 5000,
			},
			breakpoints: {
				768:{
				  	slidesPerView: 3,
				},
				991:{
				  	slidesPerView: 3,
				}
			}
		});
	}

	/* testimonial Slider JS */
	if ($('.testimonial-slider').length) {
		const testimonial_slider = new Swiper('.testimonial-slider .swiper', {
			slidesPerView : 1,
			speed: 1000,
			spaceBetween: 30,
			loop: true,
			autoplay: {
				delay: 5000,
			},
			pagination: {
				el: '.testimonial-pagination',
				clickable: true,
			},
			navigation: {
				nextEl: '.testimonial-button-next',
				prevEl: '.testimonial-button-prev',
			},
			breakpoints: {
				768:{
					slidesPerView: 1,
				},
				991:{
					slidesPerView: 1,
				}
			}
		});
	}

	/* Skill Bar */
	if ($('.skills-progress-bar').length) {
		$('.skills-progress-bar').waypoint(function() {
			$('.skillbar').each(function() {
				$(this).find('.count-bar').animate({
				width:$(this).attr('data-percent')
				},2000);
			});
		},{
			offset: '50%'
		});
	}

	/* Youtube Background Video JS */
	if ($('#herovideo').length) {
		var myPlayer = $("#herovideo").YTPlayer();
	}

	/* Init Counter */
	if ($('.counter').length) {
		$('.counter').counterUp({ delay: 6, time: 3000 });
	}

	/* Image Reveal Animation */
	if ($('.reveal').length) {
        gsap.registerPlugin(ScrollTrigger);
        let revealContainers = document.querySelectorAll(".reveal");
        revealContainers.forEach((container) => {
            let image = container.querySelector("img");
            let tl = gsap.timeline({
                scrollTrigger: {
                    trigger: container,
                    toggleActions: "play none none none"
                }
            });
            tl.set(container, {
                autoAlpha: 1
            });
            tl.from(container, 1, {
                xPercent: -100,
                ease: Power2.out
            });
            tl.from(image, 1, {
                xPercent: 100,
                scale: 1,
                delay: -1,
                ease: Power2.out
            });
        });
    }

	/* Text Effect Animation */
	if ($('.text-anime-style-1').length) {
		let staggerAmount 	= 0.05,
			translateXValue = 0,
			delayValue 		= 0.5,
		   animatedTextElements = document.querySelectorAll('.text-anime-style-1');
		
		animatedTextElements.forEach((element) => {
			let animationSplitText = new SplitText(element, { type: "chars, words" });
				gsap.from(animationSplitText.words, {
				duration: 1,
				delay: delayValue,
				x: 20,
				autoAlpha: 0,
				stagger: staggerAmount,
				scrollTrigger: { trigger: element, start: "top 85%" },
				});
		});		
	}
	
	if ($('.text-anime-style-2').length) {				
		let	 staggerAmount 		= 0.03,
			 translateXValue	= 20,
			 delayValue 		= 0.1,
			 easeType 			= "power2.out",
			 animatedTextElements = document.querySelectorAll('.text-anime-style-2');
		
		animatedTextElements.forEach((element) => {
			let animationSplitText = new SplitText(element, { type: "chars, words" });
				gsap.from(animationSplitText.chars, {
					duration: 1,
					delay: delayValue,
					x: translateXValue,
					autoAlpha: 0,
					stagger: staggerAmount,
					ease: easeType,
					scrollTrigger: { trigger: element, start: "top 85%"},
				});
		});		
	}
	
	if ($('.text-anime-style-3').length) {		
		let	animatedTextElements = document.querySelectorAll('.text-anime-style-3');
		
		 animatedTextElements.forEach((element) => {
			//Reset if needed
			if (element.animation) {
				element.animation.progress(1).kill();
				element.split.revert();
			}

			element.split = new SplitText(element, {
				type: "lines,words,chars",
				linesClass: "split-line",
			});
			gsap.set(element, { perspective: 400 });

			gsap.set(element.split.chars, {
				opacity: 0,
				x: "50",
			});

			element.animation = gsap.to(element.split.chars, {
				scrollTrigger: { trigger: element,	start: "top 90%" },
				x: "0",
				y: "0",
				rotateX: "0",
				opacity: 1,
				duration: 1,
				ease: Back.easeOut,
				stagger: 0.02,
			});
		});		
	}

	/* Parallaxie js */
	/* var $parallaxie = $('.parallaxie');
	if($parallaxie.length && ($window.width() > 991))
	{
		if ($window.width() > 768) {
			$parallaxie.parallaxie({
				speed: 0.55,
				offset: 0,
			});
		}
	} */

	/* Zoom Gallery screenshot */
	$('.gallery-items').magnificPopup({
		delegate: 'a',
		type: 'image',
		closeOnContentClick: false,
		closeBtnInside: false,
		mainClass: 'mfp-with-zoom',
		image: {
			verticalFit: true,
		},
		gallery: {
			enabled: true
		},
		zoom: {
			enabled: true,
			duration: 300, // don't foget to change the duration also in CSS
			opener: function(element) {
			  return element.find('img');
			}
		}
	});

	/* Contact form validation */
	var $contactform = $("#contactForm");
	$contactform.validator({focus: false}).on("submit", function (event) {
		if (!event.isDefaultPrevented()) {
			event.preventDefault();
			submitForm();
		}
	});

	function submitForm(){
		/* Ajax call to submit form */
		$.ajax({
			type: "POST",
			url: "form-process.php",
			data: $contactform.serialize(),
			success : function(text){
				if (text === "success"){
					formSuccess();
				} else {
					submitMSG(false,text);
				}
			}
		});
	}

	function formSuccess(){
		$contactform[0].reset();
		submitMSG(true, "Message Sent Successfully!")
	}

	function submitMSG(valid, msg){
		if(valid){
			var msgClasses = "h4 text-success";
		} else {
			var msgClasses = "h4 text-danger";
		}
		$("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
	}
	/* Contact form validation end */

	/* Animated Wow Js */	
	new WOW().init();

	/* Popup Video */
	if ($('.popup-video').length) {
		$('.popup-video').magnificPopup({
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: true
		});
	}

	/* Our Gallery (filtering) Start */
	$window.on( "load", function(){
		if( $(".gallery-item-boxes").length ) {
				
			/* Init Isotope */
			var $menuitem = $(".gallery-item-boxes").isotope({
				itemSelector: ".gallery-item-box",
				layoutMode: "masonry",
				masonry: {
					// use outer width of grid-sizer for columnWidth
					columnWidth: 1,
				}
			});
				
			/* Filter items on click */
			var $menudisesnav = $(".our-gallery-nav li a");
				$menudisesnav.on('click', function (e) { 
			
				var filterValue = $(this).attr('data-filter');
				$menuitem.isotope({
					filter: filterValue
				}); 
				
				$menudisesnav.removeClass("active-btn"); 
				$(this).addClass("active-btn");
				e.preventDefault();
			});		
			$menuitem.isotope({ filter: "*" });
		}			
	});
	/* Our Gallery (filtering) End */

	/* Service Entry Step Item Active Start */
	var $service_step_list = $('.service-entry-step-list');
	if ($service_step_list.length) {
		var $service_step = $service_step_list.find('.service-entry-step-item');

		if ($service_step.length) {
			$service_step.on({
				mouseenter: function () {
					if (!$(this).hasClass('active')) {
						$service_step.removeClass('active'); 
						$(this).addClass('active'); 
					}
				},
				mouseleave: function () {
					// Optional: Add logic for mouse leave if needed
				}
			});
		}
	}
	document.addEventListener('DOMContentLoaded', () => {
    const progressPath = document.querySelector('.progress-circle path');
    const pathLength = progressPath.getTotalLength();
    const scrollBtn = document.querySelector('.progress-wrap');

    // Initialize the circle path
    progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
    progressPath.style.strokeDasharray = `${pathLength} ${pathLength}`;
    progressPath.style.strokeDashoffset = pathLength;
    progressPath.getBoundingClientRect();
    progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';

    // Function to update the progress ring
    const updateProgress = () => {
        const scroll = window.pageYOffset || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = pathLength - (scroll * pathLength / height);
        
        progressPath.style.strokeDashoffset = progress;

        // Toggle button visibility
        if (scroll > 100) {
            scrollBtn.classList.add('active-progress');
        } else {
            scrollBtn.classList.remove('active-progress');
        }
    };

    // Smooth scroll to top
    scrollBtn.addEventListener('click', (event) => {
        event.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Listen for scroll events
    window.addEventListener('scroll', updateProgress);
});
document.addEventListener('DOMContentLoaded', () => {
    
    // --- CONFIGURATION ---
    const DEV_MOCK = true; 
    const API_ENDPOINT = 'https://YOUR_REAL_API_URL_HERE'; 
    const STORAGE_KEY = 'hulegeb_chat_v2'; 
    
    // --- DOM ELEMENTS ---
    const chatWindow = document.getElementById('chatWindow');
    const toggleBtn = document.getElementById('chatToggleBtn');
    const closeBtn = document.getElementById('closeChatBtn');
    const clearBtn = document.getElementById('clearChatBtn');
    const chatMessages = document.getElementById('chatMessages');
    const typingIndicator = document.getElementById('typingIndicator');
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendBtn');

    let isBotTyping = false;

    // --- INITIALIZATION ---
    function initChat() {
        const history = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
        
        if (history.length === 0) {
            const welcomeMsg = {
                text: "Hello! I am Hulegeb Chatbot. How can I help you today?",
                sender: 'bot',
                timestamp: new Date().toISOString()
            };
            history.push(welcomeMsg);
            localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
        }

        // Clear and prepare container
        chatMessages.innerHTML = ''; 
        
        // Safety: ensure typingIndicator is in the DOM before rendering history
        chatMessages.appendChild(typingIndicator);
        typingIndicator.style.display = 'none';

        // Render history
        history.forEach(msg => renderMessageToDOM(msg));
        
        scrollToBottom();
    }

    // --- CORE LOGIC ---
    function handleSend() {
        const text = chatInput.value.trim();
        if (!text || isBotTyping) return;

        addMessage(text, 'user');
        
        chatInput.value = '';
        chatInput.style.height = 'auto';
        sendBtn.disabled = true;

        isBotTyping = true;
        showTyping(true);

        if (DEV_MOCK) {
            getMockReply(text);
        } else {
            getRealApiReply(text);
        }
    }

    function getMockReply(userText) {
        setTimeout(() => {
            let replyText = "I am Hulegeb AI. I received your message: " + userText;
            
            if (userText.toLowerCase().includes('pi')) {
                replyText = "Pi is approximately 3.14159.";
            } else if (userText.toLowerCase().includes('hello')) {
                replyText = "Hello there! Ask me anything.";
            }

            addMessage(replyText, 'bot');
            isBotTyping = false;
            showTyping(false);
        }, 1500);
    }

    async function getRealApiReply(userText) {
        try {
            const response = await fetch(API_ENDPOINT, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userText })
            });
            const data = await response.json();
            addMessage(data.reply || "No response from server.", 'bot');
        } catch (error) {
            addMessage("Error connecting to Hulegeb Server.", 'bot');
        } finally {
            isBotTyping = false;
            showTyping(false);
        }
    }

    // --- HELPER FUNCTIONS ---
    function addMessage(text, sender) {
        const msg = { text, sender, timestamp: new Date().toISOString() };
        
        const history = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
        history.push(msg);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(history));

        renderMessageToDOM(msg);
        scrollToBottom();
    }

    function renderMessageToDOM(msg) {
        const div = document.createElement('div');
        div.className = `message ${msg.sender}-message`;
        
        const time = new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        div.innerHTML = `
            <div class="message-content">${escapeHtml(msg.text)}</div>
            <div class="message-meta">${time}</div>
        `;
        
        // --- FIXED LINE BELOW ---
        // Check if typingIndicator is actually a child of chatMessages
        if (typingIndicator && chatMessages.contains(typingIndicator)) {
            chatMessages.insertBefore(div, typingIndicator);
        } else {
            chatMessages.appendChild(div);
        }
    }

    function showTyping(show) {
        if (typingIndicator) {
            typingIndicator.style.display = show ? 'flex' : 'none';
        }
        scrollToBottom();
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function clearChat() {
        if (confirm('Clear all conversation history?')) {
            localStorage.removeItem(STORAGE_KEY);
            initChat(); 
        }
    }

    // --- EVENT LISTENERS ---
    toggleBtn.addEventListener('click', () => {
        chatWindow.classList.toggle('active');
        toggleBtn.classList.toggle('open');
        if(chatWindow.classList.contains('active')) {
            setTimeout(() => chatInput.focus(), 300);
            scrollToBottom();
        }
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.classList.remove('active');
        toggleBtn.classList.remove('open');
    });

    if (clearBtn) clearBtn.addEventListener('click', clearChat);
    sendBtn.addEventListener('click', handleSend);

    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    });

    chatInput.addEventListener('input', () => {
        chatInput.style.height = 'auto';
        chatInput.style.height = chatInput.scrollHeight + 'px';
        sendBtn.disabled = chatInput.value.trim() === '';
    });

    initChat();
});
(function() {
    const fixLayout = () => {
        const resetStyles = { margin: '0', padding: '0', width: '100%', maxWidth: '100%', overflowX: 'hidden' };
        Object.assign(document.documentElement.style, resetStyles);
        Object.assign(document.body.style, resetStyles);

        // TARGET EVERYTHING EXCEPT THE HEADER
        // I removed '.main-header' and '.navbar' from this list
        const fullWidthElements = document.querySelectorAll('.hero, footer, .footer');
        
        fullWidthElements.forEach(el => {
            el.style.width = '100%';
            el.style.left = '0';
        });
    };

    fixLayout();
    window.addEventListener('resize', fixLayout);
    setTimeout(fixLayout, 500);
})();
	
})(jQuery);