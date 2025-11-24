// ==============================================
// Navbar Scroll Effect
// ==============================================
const navbar = document.querySelector('.navbar');
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ==============================================
// Mobile Menu Toggle
// ==============================================
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        const icon = navToggle.querySelector('i');
        
        if (navMenu.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
    
    // Close menu when clicking on links
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            const icon = navToggle.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        });
    });
}

// ==============================================
// Active Navigation Link
// ==============================================
const currentPath = window.location.pathname;
navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
    }
});

// ==============================================
// Smooth Scrolling for Anchor Links
// ==============================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ==============================================
// Scroll to Top Button
// ==============================================
const scrollTopBtn = document.querySelector('.scroll-top');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        scrollTopBtn.classList.add('visible');
    } else {
        scrollTopBtn.classList.remove('visible');
    }
});

scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// ==============================================
// Stats Counter Animation (Homepage)
// ==============================================
const statsSection = document.querySelector('.stats');
if (statsSection) {
    const statNumbers = document.querySelectorAll('.stat-number');
    let animated = false;

    const animateCounter = (element) => {
        const target = parseInt(element.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                element.textContent = Math.floor(current) + (element.textContent.includes('+') ? '+' : '');
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target + (element.textContent.includes('+') ? '+' : '');
            }
        };

        updateCounter();
    };

    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animated) {
                animated = true;
                statNumbers.forEach(stat => animateCounter(stat));
            }
        });
    }, observerOptions);

    observer.observe(statsSection);
}

// ==============================================
// Typing Animation (Homepage Hero)
// ==============================================
const typingElement = document.querySelector('.typing-text');
if (typingElement) {
    const texts = [
        'Full Stack Developer',
        'Python Enthusiast',
        'Problem Solver',
        'API Designer'
    ];
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function type() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            typingElement.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 50;
        } else {
            typingElement.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 100;
        }

        if (!isDeleting && charIndex === currentText.length) {
            isDeleting = true;
            typingSpeed = 2000;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typingSpeed = 500;
        }

        setTimeout(type, typingSpeed);
    }

    type();
}

// ==============================================
// Project Filtering (Projects Page)
// ==============================================
const filterButtons = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

if (filterButtons.length > 0) {
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const filter = button.getAttribute('data-filter');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                
                if (filter === 'all' || category === filter) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 10);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
}

// ==============================================
// Project Modal (Projects Page)
// ==============================================
const modal = document.querySelector('.modal');
const modalClose = document.querySelector('.modal-close');
const projectCardsWithModal = document.querySelectorAll('.project-card[data-project]');

if (modal && projectCardsWithModal.length > 0) {
    projectCardsWithModal.forEach(card => {
        card.addEventListener('click', () => {
            const projectData = JSON.parse(card.getAttribute('data-project'));
            
            // Populate modal with project data
            document.querySelector('.modal-content h2').textContent = projectData.title;
            document.querySelector('.modal-content p').textContent = projectData.description;
            
            // Add technologies if available
            const techList = document.querySelector('.modal-technologies');
            if (techList && projectData.tech) {
                techList.innerHTML = projectData.tech.map(tech => 
                    `<span class="project-tag">${tech}</span>`
                ).join('');
            }
            
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    // Close modal
    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    };

    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

// ==============================================
// Contact Form Validation
// ==============================================
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const subject = document.getElementById('subject').value.trim();
        const message = document.getElementById('message').value.trim();

        // Basic validation
        if (!name || !email || !subject || !message) {
            e.preventDefault();
            alert('Please fill in all fields');
            return;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            e.preventDefault();
            alert('Please enter a valid email address');
            return;
        }

        // If validation passes, show loading state
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitBtn.disabled = true;
    });
}

// ==============================================
// Flash Messages Auto-dismiss
// ==============================================
const flashMessages = document.querySelectorAll('.flash-message');
if (flashMessages.length > 0) {
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
}

// ==============================================
// FAQ Accordion (Contact Page)
// ==============================================
// Note: FAQ accordion is now handled in contact.html template
// to avoid variable conflicts and ensure proper initialization

// ==============================================
// Code Window Animation (Homepage)
// ==============================================
const codeWindow = document.querySelector('.code-window');
if (codeWindow) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                codeWindow.style.animation = 'fadeInUp 0.8s ease';
            }
        });
    }, { threshold: 0.3 });

    observer.observe(codeWindow);
}

// Add fadeInUp animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideOutRight {
        to {
            opacity: 0;
            transform: translateX(100%);
        }
    }
`;
document.head.appendChild(style);

// ==============================================
// Parallax Effect for Background Shapes
// ==============================================
const bgShapes = document.querySelectorAll('.bg-shape');
if (bgShapes.length > 0) {
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        bgShapes.forEach((shape, index) => {
            const speed = 0.5 + (index * 0.2);
            const yPos = -(scrolled * speed);
            shape.style.transform = `translateY(${yPos}px)`;
        });
    });
}

// ==============================================
// Lazy Loading for Images (if any)
// ==============================================
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    const lazyImages = document.querySelectorAll('img[data-src]');
    lazyImages.forEach(img => imageObserver.observe(img));
}

// ==============================================
// Performance: Debounce Scroll Events
// ==============================================
function debounce(func, wait) {
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

// Apply debounce to scroll-heavy operations
const debouncedParallax = debounce(() => {
    const scrolled = window.scrollY;
    bgShapes.forEach((shape, index) => {
        const speed = 0.5 + (index * 0.2);
        const yPos = -(scrolled * speed);
        shape.style.transform = `translateY(${yPos}px)`;
    });
}, 10);

if (bgShapes.length > 0) {
    window.addEventListener('scroll', debouncedParallax);
}

// ==============================================
// Console Easter Egg
// ==============================================
console.log('%c👋 Hello, Developer!', 'font-size: 20px; font-weight: bold; color: #667eea;');
console.log('%cLooking for something? Check out the source code on GitHub!', 'font-size: 14px; color: #94a3b8;');
console.log('%cBuilt with ❤️ using Flask, HTML, CSS, and JavaScript By Soumya 🚀', 'font-size: 12px; color: #64748b;');

// ==============================================
// Initialize on Load
// ==============================================
document.addEventListener('DOMContentLoaded', () => {
    // Add loaded class to body for CSS transitions
    document.body.classList.add('loaded');
    
    // Log page load time (for development)
    if (window.performance) {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log(`Page loaded in ${pageLoadTime}ms`);
    }
});
