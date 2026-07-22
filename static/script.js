const searchInput = document.getElementById('materialSearch');
const cards = Array.from(document.querySelectorAll('.material-card'));

if (searchInput) {
    searchInput.addEventListener('input', (event) => {
        const query = event.target.value.trim().toLowerCase();

        cards.forEach((card) => {
            const content = card.dataset.search.toLowerCase();
            const match = content.includes(query);
            card.classList.toggle('is-hidden', !match);
        });
    });
}

const folderTriggers = document.querySelectorAll('.folder-trigger');

folderTriggers.forEach((trigger) => {
    trigger.addEventListener('click', () => {
        const card = trigger.closest('.folder-card');
        const isOpen = card.classList.contains('open');

        document.querySelectorAll('.folder-card.open').forEach((item) => {
            item.classList.remove('open');
            item.querySelector('.folder-trigger').setAttribute('aria-expanded', 'false');
        });

        if (!isOpen) {
            card.classList.add('open');
            trigger.setAttribute('aria-expanded', 'true');
        }
    });
});
