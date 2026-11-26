// Small progressive enhancement: indicate active dashboard section while scrolling.
const navLinks = [...document.querySelectorAll('.side a')];
const sections = navLinks.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        navLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`));
      }
    }
  }, { rootMargin: '-15% 0px -70% 0px' });
  sections.forEach(section => observer.observe(section));
}
