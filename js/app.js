'use strict';

(function () {
  document.addEventListener('DOMContentLoaded', function () {
    const html = document.documentElement;
    const toggleBtn = document.getElementById('theme-toggle');

    // --- Theme toggle ---

    function getInitialTheme() {
      const stored = localStorage.getItem('theme');
      if (stored === 'light' || stored === 'dark') {
        return stored;
      }
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        return 'light';
      }
      return 'dark';
    }

    function applyTheme(theme) {
      if (theme === 'light') {
        html.setAttribute('data-theme', 'light');
        toggleBtn.setAttribute('aria-label', 'Switch to dark theme');
      } else {
        html.removeAttribute('data-theme');
        toggleBtn.setAttribute('aria-label', 'Switch to light theme');
      }
    }

    applyTheme(getInitialTheme());

    toggleBtn.addEventListener('click', function () {
      const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      applyTheme(next);
      localStorage.setItem('theme', next);
    });

    // --- Nav scrolled state ---

    const nav = document.getElementById('nav');

    window.addEventListener('scroll', function () {
      if (window.scrollY > 0) {
        nav.classList.add('nav--scrolled');
      } else {
        nav.classList.remove('nav--scrolled');
      }
    }, { passive: true });

    // --- Scroll spy ---

    const navLinks = document.querySelectorAll('.nav__link');
    const sections = document.querySelectorAll('section[id]');

    // Map section id → nav link
    const sectionLinkMap = {};
    navLinks.forEach(function (link) {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        sectionLinkMap[href.slice(1)] = link;
      }
    });

    // Track sections currently in the scroll-spy zone
    const spySections = new Set();
    let spyRafId = null;

    function updateActiveLink() {
      spyRafId = null;
      if (spySections.size === 0) return;

      // Among intersecting sections, activate the topmost one (smallest getBoundingClientRect().top)
      let topmost = null;
      let topmostTop = Infinity;
      spySections.forEach(function (section) {
        const top = section.getBoundingClientRect().top;
        if (top < topmostTop) {
          topmostTop = top;
          topmost = section;
        }
      });

      navLinks.forEach(function (l) { l.classList.remove('nav__link--active'); });
      if (topmost) {
        const link = sectionLinkMap[topmost.id];
        if (link) link.classList.add('nav__link--active');
      }
    }

    // Activate the nav link for the topmost section in the upper-middle viewport zone.
    // rAF debounce ensures that when multiple entries fire simultaneously (fast scroll),
    // all intersection updates are batched before the topmost section is selected.
    const sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          spySections.add(entry.target);
        } else {
          spySections.delete(entry.target);
        }
      });
      if (spyRafId === null) {
        spyRafId = requestAnimationFrame(updateActiveLink);
      }
    }, {
      rootMargin: '-10% 0px -60% 0px',
      threshold: 0
    });

    sections.forEach(function (section) {
      sectionObserver.observe(section);
    });

    // --- Mobile hamburger menu ---

    const hamburgerBtn = document.getElementById('nav-hamburger');

    function closeMenu(returnFocus) {
      nav.classList.remove('nav--open');
      hamburgerBtn.setAttribute('aria-expanded', 'false');
      hamburgerBtn.setAttribute('aria-label', 'Open navigation menu');
      if (returnFocus) {
        hamburgerBtn.focus();
      }
    }

    hamburgerBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      const isOpen = nav.classList.toggle('nav--open');
      hamburgerBtn.setAttribute('aria-expanded', String(isOpen));
      hamburgerBtn.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
    });

    // Close when a nav link is clicked
    navLinks.forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });

    // Close when clicking outside the nav
    document.addEventListener('click', function (e) {
      if (!nav.contains(e.target)) {
        closeMenu();
      }
    });

    // Close on Escape key — return focus to hamburger (WAI-ARIA Disclosure pattern)
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('nav--open')) {
        closeMenu(true);
      }
    });

    // Close when resizing to desktop
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 768) {
        closeMenu();
      }
    }, { passive: true });

    // --- Back to top button ---

    const backToTopBtn = document.getElementById('back-to-top');

    window.addEventListener('scroll', function () {
      if (window.scrollY > window.innerHeight) {
        backToTopBtn.classList.add('back-to-top--visible');
      } else {
        backToTopBtn.classList.remove('back-to-top--visible');
      }
    }, { passive: true });

    backToTopBtn.addEventListener('click', function () {
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'instant' : 'smooth' });
    });

    // --- Scroll animations ---

    const animObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          animObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    sections.forEach(function (section) {
      if (section.id === 'hero') {
        // Hero is immediately visible — no fade-in on load
        section.classList.add('is-visible');
      } else {
        animObserver.observe(section);
      }
    });
  });
}());
