'use strict';

(function () {
  document.addEventListener('DOMContentLoaded', function () {
    const html = document.documentElement;
    const toggleBtn = document.getElementById('theme-toggle');

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
  });
}());
