document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const navBtns = document.querySelectorAll('.glass-btn');
    const cards = document.querySelectorAll('.glass-card');
    const logoContainer = document.getElementById('logoContainer');
    const backBtn = document.getElementById('backBtn');
    const dropdownToggle = document.getElementById('dropdownToggle');
    const dropdownContent = document.getElementById('dropdownContent');
    const categoryTitle = document.getElementById('categoryTitle');

    const goHome = () => {
        body.classList.add('state-home');
        navBtns.forEach(b => b.classList.remove('active'));
        cards.forEach(card => card.classList.remove('visible'));
        dropdownContent.classList.remove('show');
    };

    logoContainer.addEventListener('click', goHome);
    backBtn.addEventListener('click', goHome);

    dropdownToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdownContent.classList.toggle('show');
    });

    document.addEventListener('click', (e) => {
        if (!dropdownContent.contains(e.target) && !dropdownToggle.contains(e.target)) {
            dropdownContent.classList.remove('show');
        }
    });

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (body.classList.contains('state-home')) {
                body.classList.remove('state-home');
            }

            navBtns.forEach(b => b.classList.remove('active'));
            
            const targetCategory = btn.getAttribute('data-target');
            document.querySelectorAll(`.glass-btn[data-target="${targetCategory}"]`).forEach(b => {
                b.classList.add('active');
            });

            // Обновляем заголовок (используем textContent кнопки без учета SVG)
            // Берем только текстовый span
            const btnSpan = btn.querySelector('span');
            if(btnSpan) {
                categoryTitle.textContent = btnSpan.textContent.trim();
            } else {
                categoryTitle.textContent = btn.textContent.trim();
            }

            dropdownContent.classList.remove('show');

            cards.forEach(card => {
                if (card.getAttribute('data-category') === targetCategory) {
                    card.classList.add('visible');
                } else {
                    card.classList.remove('visible');
                }
            });
        });
    });

    const recolorBtns = document.querySelectorAll('.recolor-btn');
    recolorBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Снимаем выделение со всех кнопок в меню
            navBtns.forEach(b => b.classList.remove('active'));
            
            const targetCategory = btn.getAttribute('data-target');
            categoryTitle.textContent = "ПЕРЕКРАСЫ Y2K";

            cards.forEach(card => {
                if (card.getAttribute('data-category') === targetCategory) {
                    card.classList.add('visible');
                } else {
                    card.classList.remove('visible');
                }
            });
            // Прокручиваем к заголовку, чтобы пользователь сразу видел перекрасы
            categoryTitle.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    // === КОПИРОВАНИЕ ПРОМПТОВ СТИЛЕЙ ===
    const copyBtns = document.querySelectorAll('.copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const textToCopy = btn.getAttribute('data-text');
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalHTML = btn.innerHTML;
                btn.classList.add('copied');
                btn.innerHTML = '<svg class="svg-icon" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg> <span>Скопировано!</span>';
                
                setTimeout(() => {
                    btn.classList.remove('copied');
                    btn.innerHTML = originalHTML;
                }, 2000);
            });
        });
    });

    // === КАРАУСЕЛЬ В КАРТОЧКАХ ===
    const carouselWrappers = document.querySelectorAll('.carousel-wrapper');
    carouselWrappers.forEach(wrapper => {
        const imagesContainer = wrapper.querySelector('.carousel-images');
        const prevArrow = wrapper.querySelector('.prev-arrow');
        const nextArrow = wrapper.querySelector('.next-arrow');

        if(prevArrow && nextArrow && imagesContainer) {
            prevArrow.addEventListener('click', (e) => {
                e.stopPropagation(); // Не открывать лайтбокс при клике на стрелку
                imagesContainer.scrollBy({ left: -imagesContainer.clientWidth, behavior: 'smooth' });
            });
            nextArrow.addEventListener('click', (e) => {
                e.stopPropagation();
                imagesContainer.scrollBy({ left: imagesContainer.clientWidth, behavior: 'smooth' });
            });
        }
    });

    // === ЛАЙТБОКС (ГАЛЕРЕЯ) ===
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxClose = document.getElementById('lightboxClose');
    const lightboxPrev = document.getElementById('lightboxPrev');
    const lightboxNext = document.getElementById('lightboxNext');
    
    let currentGallery = [];
    let currentIndex = 0;

    const allCardImgs = document.querySelectorAll('.card-img');

    allCardImgs.forEach(img => {
        img.addEventListener('click', () => {
            // Ищем все картинки в текущей карточке (если это карусель)
            const parentContainer = img.closest('.carousel-images') || img.parentElement;
            currentGallery = Array.from(parentContainer.querySelectorAll('.card-img'));
            currentIndex = currentGallery.indexOf(img);

            updateLightboxImage();
            
            lightbox.classList.add('show');
            body.style.overflow = 'hidden';
            
            // Скрываем стрелки лайтбокса, если картинка всего одна
            if(currentGallery.length <= 1) {
                if(lightboxPrev) lightboxPrev.style.display = 'none';
                if(lightboxNext) lightboxNext.style.display = 'none';
            } else {
                if(lightboxPrev) lightboxPrev.style.display = 'flex';
                if(lightboxNext) lightboxNext.style.display = 'flex';
            }
        });
    });

    const updateLightboxImage = () => {
        if(currentGallery.length > 0) {
            lightboxImg.src = currentGallery[currentIndex].src;
        }
    };

    if(lightboxPrev) {
        lightboxPrev.addEventListener('click', (e) => {
            e.stopPropagation();
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : currentGallery.length - 1;
            updateLightboxImage();
        });
    }

    if(lightboxNext) {
        lightboxNext.addEventListener('click', (e) => {
            e.stopPropagation();
            currentIndex = (currentIndex < currentGallery.length - 1) ? currentIndex + 1 : 0;
            updateLightboxImage();
        });
    }

    const closeLightbox = () => {
        lightbox.classList.remove('show');
        body.style.overflow = 'auto';
        setTimeout(() => {
            if(!lightbox.classList.contains('show')) lightboxImg.src = "";
        }, 300);
    };

    lightboxClose.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImg && !e.target.closest('.lightbox-nav')) {
            closeLightbox();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (infoModal && infoModal.classList.contains('show') && e.key === 'Escape') {
            closeInfoModal();
            return;
        }
        
        if (!lightbox.classList.contains('show')) return;
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : currentGallery.length - 1;
            updateLightboxImage();
        }
        if (e.key === 'ArrowRight') {
            currentIndex = (currentIndex < currentGallery.length - 1) ? currentIndex + 1 : 0;
            updateLightboxImage();
        }
    });

    // === ИНФО-МОДАЛКА ДЛЯ РАСШИРЕНИЙ ===
    const infoModal = document.getElementById('infoModal');
    const infoModalClose = document.getElementById('infoModalClose');
    const infoModalImg = document.getElementById('infoModalImg');
    const infoModalTitle = document.getElementById('infoModalTitle');
    const infoModalDesc = document.getElementById('infoModalDesc');
    const infoBtns = document.querySelectorAll('.info-btn');

    infoBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const card = btn.closest('.glass-card');
            const dataContainer = card.querySelector('.info-data');
            if (dataContainer && infoModal) {
                const title = dataContainer.querySelector('.info-title').innerHTML;
                const img = dataContainer.querySelector('.info-img').textContent.trim();
                const desc = dataContainer.querySelector('.info-desc').innerHTML;

                infoModalTitle.innerHTML = title;
                infoModalImg.src = img;
                infoModalDesc.innerHTML = desc;

                infoModal.classList.add('show');
                body.style.overflow = 'hidden';
            }
        });
    });

    const closeInfoModal = () => {
        if(infoModal) {
            infoModal.classList.remove('show');
            body.style.overflow = 'auto';
        }
    };

    if(infoModalClose) infoModalClose.addEventListener('click', closeInfoModal);

    if(infoModal) {
        infoModal.addEventListener('click', (e) => {
            if (e.target === infoModal) {
                closeInfoModal();
            }
        });
    }

});
