(() => {
  const shots = () => Array.from(document.querySelectorAll('[data-lightbox]'));

  let overlay = null;
  let imgEl = null;
  let index = 0;
  let items = [];

  function ensureOverlay() {
    if (overlay) return overlay;
    overlay = document.createElement('div');
    overlay.className = 'lightbox';
    overlay.setAttribute('hidden', '');
    overlay.innerHTML = `
      <button type="button" class="lightbox-close" aria-label="Close">&times;</button>
      <button type="button" class="lightbox-nav lightbox-prev" aria-label="Previous">‹</button>
      <figure class="lightbox-figure">
        <img class="lightbox-img" alt="" />
      </figure>
      <button type="button" class="lightbox-nav lightbox-next" aria-label="Next">›</button>
    `;
    document.body.appendChild(overlay);
    imgEl = overlay.querySelector('.lightbox-img');

    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) close();
    });
    overlay.querySelector('.lightbox-close').addEventListener('click', close);
    overlay.querySelector('.lightbox-prev').addEventListener('click', () => show(index - 1));
    overlay.querySelector('.lightbox-next').addEventListener('click', () => show(index + 1));
    return overlay;
  }

  function show(i) {
    if (!items.length) return;
    index = (i + items.length) % items.length;
    const item = items[index];
    ensureOverlay();
    imgEl.src = item.href;
    imgEl.alt = item.querySelector('img')?.alt || '';
    overlay.removeAttribute('hidden');
    document.body.classList.add('lightbox-open');
  }

  function close() {
    if (!overlay) return;
    overlay.setAttribute('hidden', '');
    document.body.classList.remove('lightbox-open');
    imgEl.removeAttribute('src');
  }

  document.addEventListener('click', (e) => {
    const link = e.target.closest('[data-lightbox]');
    if (!link) return;
    e.preventDefault();
    items = shots();
    const i = items.indexOf(link);
    show(i < 0 ? 0 : i);
  });

  document.addEventListener('keydown', (e) => {
    if (!overlay || overlay.hasAttribute('hidden')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(index - 1);
    if (e.key === 'ArrowRight') show(index + 1);
  });
})();
