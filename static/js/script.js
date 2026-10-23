/* =========================================================
   BIKASH BELBASE — EDUCATION CONSULTANT PORTFOLIO
   File: static/js/script.js
   Compatible with: HTML + CSS + Django Templates
   ========================================================= */

"use strict";

/* =========================================================
   1. DOM READY
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {
    initializeNavigation();
    initializeSmoothScrolling();
    initializeHeader();
    initializeScrollAnimations();
    initializeActiveNavigation();
    initializeBackToTop();
    initializeCurrentYear();
    initializeContactForm();
    initializeImageHandling();
    initializeCounters();
});


/* =========================================================
   2. RESPONSIVE MOBILE NAVIGATION
   Supports .is-open and .is-active classes
   ========================================================= */

function initializeNavigation() {
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (!menuToggle || !navLinks) return;

    function closeMenu() {
        navLinks.classList.remove("is-open");
        menuToggle.classList.remove("is-active");
        menuToggle.setAttribute("aria-expanded", "false");
    }

    function toggleMenu() {
        const isOpen = navLinks.classList.toggle("is-open");

        menuToggle.classList.toggle("is-active", isOpen);
        menuToggle.setAttribute("aria-expanded", String(isOpen));
    }

    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-controls", "navLinks");

    menuToggle.addEventListener("click", function (event) {
        event.stopPropagation();
        toggleMenu();
    });

    // Close menu after selecting a navigation link.
    navLinks.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", closeMenu);
    });

    // Close menu when clicking outside it.
    document.addEventListener("click", function (event) {
        if (
            !navLinks.contains(event.target) &&
            !menuToggle.contains(event.target)
        ) {
            closeMenu();
        }
    });

    // Close menu with Escape.
    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeMenu();
            menuToggle.focus();
        }
    });

    // Close mobile menu when returning to desktop layout.
    window.addEventListener("resize", function () {
        if (window.innerWidth > 820) {
            closeMenu();
        }
    });
}


/* =========================================================
   3. SMOOTH SCROLLING
   For links such as #about, #services and #contact
   ========================================================= */

function initializeSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    anchorLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            const targetId = link.getAttribute("href");

            if (!targetId || targetId === "#") return;

            const targetElement = document.querySelector(targetId);

            if (!targetElement) return;

            event.preventDefault();

            targetElement.scrollIntoView({
                behavior: window.matchMedia(
                    "(prefers-reduced-motion: reduce)"
                ).matches ? "auto" : "smooth",
                block: "start"
            });

            // Update the URL hash without jumping to the target.
            if (history.pushState) {
                history.pushState(null, "", targetId);
            }
        });
    });
}


/* =========================================================
   4. STICKY HEADER EFFECT
   Adds .scrolled when the page moves down
   ========================================================= */

function initializeHeader() {
    const header = document.querySelector(".site-header");

    if (!header) return;

    function updateHeader() {
        header.classList.toggle("scrolled", window.scrollY > 30);
    }

    updateHeader();

    window.addEventListener("scroll", updateHeader, {
        passive: true
    });
}


/* =========================================================
   5. SCROLL REVEAL ANIMATIONS
   Optional CSS class: .reveal
   ========================================================= */

function initializeScrollAnimations() {
    const elements = document.querySelectorAll(
        ".reveal, .service-card, .destination-card, " +
        ".experience-card, .testimonial-card, .success-card"
    );

    if (!elements.length) return;

    // Respect reduced-motion preferences.
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        elements.forEach(function (element) {
            element.classList.add("is-visible");
        });
        return;
    }

    if (!("IntersectionObserver" in window)) {
        elements.forEach(function (element) {
            element.classList.add("is-visible");
        });
        return;
    }

    const observer = new IntersectionObserver(
        function (entries, currentObserver) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    currentObserver.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.12,
            rootMargin: "0px 0px -35px 0px"
        }
    );

    elements.forEach(function (element) {
        element.classList.add("reveal");
        observer.observe(element);
    });
}


/* =========================================================
   6. ACTIVE NAVIGATION LINK
   Highlights the section currently in view
   ========================================================= */

function initializeActiveNavigation() {
    const navLinks = document.querySelectorAll(
        '#navLinks a[href^="#"]'
    );

    if (!navLinks.length || !("IntersectionObserver" in window)) {
        return;
    }

    const sections = Array.from(navLinks)
        .map(function (link) {
            const selector = link.getAttribute("href");

            try {
                return document.querySelector(selector);
            } catch (error) {
                return null;
            }
        })
        .filter(Boolean);

    if (!sections.length) return;

    const sectionObserver = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;

                const currentId = "#" + entry.target.id;

                navLinks.forEach(function (link) {
                    const isCurrent =
                        link.getAttribute("href") === currentId;

                    if (isCurrent) {
                        link.classList.add("active");
                        link.setAttribute("aria-current", "location");
                    } else {
                        link.classList.remove("active");
                        link.removeAttribute("aria-current");
                    }
                });
            });
        },
        {
            rootMargin: "-30% 0px -60% 0px",
            threshold: 0
        }
    );

    sections.forEach(function (section) {
        sectionObserver.observe(section);
    });
}


/* =========================================================
   7. BACK TO TOP BUTTON
   Works with an element having id="backToTop"
   ========================================================= */

function initializeBackToTop() {
    const backToTop = document.getElementById("backToTop");

    if (!backToTop) return;

    function updateButton() {
        const shouldShow = window.scrollY > 400;

        backToTop.classList.toggle("is-visible", shouldShow);
        backToTop.setAttribute("aria-hidden", String(!shouldShow));
    }

    backToTop.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: window.matchMedia(
                "(prefers-reduced-motion: reduce)"
            ).matches ? "auto" : "smooth"
        });
    });

    updateButton();

    window.addEventListener("scroll", updateButton, {
        passive: true
    });
}


/* =========================================================
   8. AUTOMATIC CURRENT YEAR
   Works with elements having id="currentYear"
   ========================================================= */

function initializeCurrentYear() {
    const yearElements = document.querySelectorAll("#currentYear");

    yearElements.forEach(function (element) {
        element.textContent = new Date().getFullYear();
    });
}


/* =========================================================
   9. CONTACT FORM VALIDATION
   Django handles actual form submission and email processing.
   This JavaScript validates fields before submission.
   ========================================================= */

function initializeContactForm() {
    const contactForm = document.getElementById("contactForm");

    if (!contactForm) return;

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    function getField(name) {
        return contactForm.querySelector(
            '[name="' + name + '"]'
        );
    }

    function showError(field, message) {
        if (!field) return;

        field.setCustomValidity(message);
        field.setAttribute("aria-invalid", "true");
    }

    function clearError(field) {
        if (!field) return;

        field.setCustomValidity("");
        field.removeAttribute("aria-invalid");
    }

    // Clear custom errors as the visitor edits the field.
    contactForm.querySelectorAll("input, textarea, select").forEach(
        function (field) {
            field.addEventListener("input", function () {
                clearError(field);
            });

            field.addEventListener("change", function () {
                clearError(field);
            });
        }
    );

    contactForm.addEventListener("submit", function (event) {
        let firstInvalidField = null;

        const nameField = getField("name");
        const emailField = getField("email");
        const phoneField = getField("phone");
        const messageField = getField("message");

        const fieldsToValidate = [
            nameField,
            emailField,
            phoneField,
            messageField
        ].filter(Boolean);

        fieldsToValidate.forEach(clearError);

        if (nameField && nameField.value.trim().length < 2) {
            showError(
                nameField,
                "Please enter your name (at least 2 characters)."
            );
            firstInvalidField = firstInvalidField || nameField;
        }

        if (
            emailField &&
            !emailPattern.test(emailField.value.trim())
        ) {
            showError(
                emailField,
                "Please enter a valid email address."
            );
            firstInvalidField = firstInvalidField || emailField;
        }

        if (phoneField && phoneField.value.trim()) {
            const digits = phoneField.value.replace(/\D/g, "");

            if (digits.length < 7 || digits.length > 15) {
                showError(
                    phoneField,
                    "Please enter a valid phone number."
                );
                firstInvalidField = firstInvalidField || phoneField;
            }
        }

        if (
            messageField &&
            messageField.value.trim().length < 10
        ) {
            showError(
                messageField,
                "Please enter a message of at least 10 characters."
            );
            firstInvalidField = firstInvalidField || messageField;
        }

        if (firstInvalidField) {
            event.preventDefault();
            firstInvalidField.focus();
            firstInvalidField.reportValidity();
            return;
        }

        // Do not prevent the default submission here.
        // Django must receive the form to save/process it.
    });
}


/* =========================================================
   10. IMAGE ERROR HANDLING
   Shows a fallback if an image cannot load.
   ========================================================= */

function initializeImageHandling() {
    const images = document.querySelectorAll("img");

    images.forEach(function (img) {
        img.addEventListener("error", function () {
            img.classList.add("image-error");

            // Keep the layout intact and avoid repeated error events.
            img.setAttribute("data-image-error", "true");
        }, { once: true });
    });
}


/* =========================================================
   11. ANIMATED NUMBER COUNTERS
   Optional markup:
   <span class="counter" data-target="500">0</span>
   ========================================================= */

function initializeCounters() {
    const counters = document.querySelectorAll(".counter");

    if (!counters.length) return;

    function setFinalValue(counter) {
        const target = Number(counter.dataset.target);

        if (Number.isFinite(target)) {
            counter.textContent = target.toLocaleString();
        }
    }

    if (
        window.matchMedia("(prefers-reduced-motion: reduce)").matches ||
        !("IntersectionObserver" in window)
    ) {
        counters.forEach(setFinalValue);
        return;
    }

    const counterObserver = new IntersectionObserver(
        function (entries, observer) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;

                const counter = entry.target;
                const target = Number(counter.dataset.target);

                if (!Number.isFinite(target)) {
                    observer.unobserve(counter);
                    return;
                }

                const duration = 1500;
                const startTime = performance.now();

                function animateCounter(currentTime) {
                    const progress = Math.min(
                        (currentTime - startTime) / duration,
                        1
                    );

                    // Ease-out effect.
                    const easedProgress = 1 - Math.pow(1 - progress, 3);
                    const currentValue = Math.floor(
                        target * easedProgress
                    );

                    counter.textContent =
                        currentValue.toLocaleString();

                    if (progress < 1) {
                        requestAnimationFrame(animateCounter);
                    } else {
                        counter.textContent = target.toLocaleString();
                    }
                }

                requestAnimationFrame(animateCounter);
                observer.unobserve(counter);
            });
        },
        {
            threshold: 0.5
        }
    );

    counters.forEach(function (counter) {
        counterObserver.observe(counter);
    });
}


/* =========================================================
   12. OPTIONAL CONSOLE MESSAGE
   ========================================================= */

console.info(
    "Bikash Belbase Portfolio: JavaScript initialized successfully."
);
