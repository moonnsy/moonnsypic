document.addEventListener('DOMContentLoaded', () => {
    // === THEME TOGGLE (АДАПТИВНАЯ ТЕМА) ===
    const themeBtn = document.getElementById('themeToggleBtn');
    
    // Проверяем сохраненную тему или системные настройки
    let savedTheme = localStorage.getItem('moonnsy-theme');
    if (!savedTheme) {
        savedTheme = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    if (themeBtn) {
        const setIcon = (theme) => {
            themeBtn.innerHTML = theme === 'dark' 
                ? '<svg viewBox="0 0 24 24" class="theme-icon" style="width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>' 
                : '<svg viewBox="0 0 24 24" class="theme-icon" style="width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
        };
        setIcon(savedTheme);

        themeBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('moonnsy-theme', newTheme);
            setIcon(newTheme);
        });
    }

    // Слушаем изменение системной темы (если юзер поменял в ОС)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (!localStorage.getItem('moonnsy-theme')) {
            const newTheme = e.matches ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', newTheme);
            if (themeBtn) {
                const setIcon = (theme) => {
                    themeBtn.innerHTML = theme === 'dark' 
                        ? '<svg viewBox="0 0 24 24" class="theme-icon" style="width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>' 
                        : '<svg viewBox="0 0 24 24" class="theme-icon" style="width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
                };
                setIcon(newTheme);
            }
        }
    });

    // === АНИМАЦИЯ ЗВЕЗДОЧЕК ===
    const createStars = () => {
        const starsContainer = document.createElement('div');
        starsContainer.className = 'stars-container';
        document.body.appendChild(starsContainer);

        const shapes = [
            '<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87L18.18 22 12 18.56 5.82 22 7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
            '<svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>',
            '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/></svg>',
            '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3z"/></svg>',
        ];

        for (let i = 0; i < 25; i++) {
            const star = document.createElement('div');
            star.className = 'floating-star';
            star.innerHTML = shapes[Math.floor(Math.random() * shapes.length)];
            star.style.left = `${Math.random() * 100}vw`;
            star.style.animationDuration = `${Math.random() * 12 + 8}s`;
            star.style.animationDelay = `${Math.random() * 8}s`;
            const size = Math.random() * 12 + 8;
            star.querySelector('svg').style.width = size + 'px';
            star.querySelector('svg').style.height = size + 'px';
            starsContainer.appendChild(star);
        }
    };
    createStars();

    // === КАРАУСЕЛЬ В КАРТОЧКАХ ===
    const carouselWrappers = document.querySelectorAll('.carousel-wrapper');
    carouselWrappers.forEach(wrapper => {
        const imagesContainer = wrapper.querySelector('.carousel-images');
        const prevArrow = wrapper.querySelector('.prev-arrow');
        const nextArrow = wrapper.querySelector('.next-arrow');

        if(imagesContainer) {
            const images = imagesContainer.querySelectorAll('img');
            
            // Функция обновления высоты карусели
            const updateHeight = () => {
                if (images.length === 0) return;
                const containerWidth = imagesContainer.getBoundingClientRect().width;
                if (containerWidth === 0) return;
                
                let index = Math.round(imagesContainer.scrollLeft / containerWidth);
                if (index < 0) index = 0;
                if (index >= images.length) index = images.length - 1;
                
                const currentImg = images[index];
                if (currentImg && currentImg.offsetHeight > 0) {
                    imagesContainer.style.height = currentImg.offsetHeight + 'px';
                }
            };

            // Слушаем скролл и изменение размера
            imagesContainer.addEventListener('scroll', updateHeight);
            window.addEventListener('resize', updateHeight);
            images.forEach(img => img.addEventListener('load', updateHeight));
            setTimeout(updateHeight, 100);

            // Предотвращаем случайное пролистывание колесиком мыши (блокируем горизонтальный скролл)
            imagesContainer.addEventListener('wheel', (e) => {
                if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) {
                    e.preventDefault();
                }
            }, { passive: false });

            if(prevArrow && nextArrow) {
                const scrollOneImage = (direction) => {
                    if (images.length === 0) return;
                    const imgWidth = images[0].getBoundingClientRect().width;
                    imagesContainer.scrollBy({ left: direction * imgWidth, behavior: 'smooth' });
                };
                
                prevArrow.addEventListener('click', (e) => {
                    e.stopPropagation();
                    scrollOneImage(-1);
                });
                nextArrow.addEventListener('click', (e) => {
                    e.stopPropagation();
                    scrollOneImage(1);
                });
            }
        }
    });

    // === КОПИРОВАНИЕ ПРОМПТОВ (на карточках) ===
    const copyPromptBtns = document.querySelectorAll('.copy-prompt-btn');
    copyPromptBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const wrapper = btn.closest('.card-img-wrapper') || btn.closest('.prompt-img-wrapper');
            const img = wrapper ? wrapper.querySelector('.card-img') : null;
            if (img && img.hasAttribute('data-prompt')) {
                const textToCopy = img.getAttribute('data-prompt');
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const originalHTML = btn.innerHTML;
                    btn.classList.add('copied');
                    btn.innerHTML = '<svg class="svg-icon" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                    setTimeout(() => {
                        btn.classList.remove('copied');
                        btn.innerHTML = originalHTML;
                    }, 2000);
                });
            }
        });
    });

    // === КНОПКА "ПОДРОБНЕЕ" ===
    const viewBtns = document.querySelectorAll('.view-btn:not(.copy-btn):not(.recolor-btn):not(.info-btn)');
    viewBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (btn.tagName === 'A') return;
            e.stopPropagation();
            const card = btn.closest('.retro-window');
            if (card) {
                const mainImg = card.querySelector('.card-img');
                if (mainImg) mainImg.click();
            }
        });
    });

    // === КНОПКА "ПЕРЕКРАСЫ" ===
    const recolorBtns = document.querySelectorAll('.recolor-btn');
    recolorBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            window.location.href = 'recolors.html';
        });
    });

    // === INFO MODAL ===
    const infoBtns = document.querySelectorAll('.info-btn');
    const infoModal = document.getElementById('infoModal');
    if (infoModal) {
        const infoModalClose = document.getElementById('infoModalClose');
        const infoModalTitle = document.getElementById('infoModalTitle');
        const infoModalImg = document.getElementById('infoModalImg');
        const infoModalDesc = document.getElementById('infoModalDesc');

        infoBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const card = btn.closest('.retro-window');
                const dataContainer = card.querySelector('.info-data');
                if (dataContainer) {
                    const title = dataContainer.querySelector('.info-title')?.innerHTML || '';
                    const img = dataContainer.querySelector('.info-img')?.textContent.trim() || '';
                    const desc = dataContainer.querySelector('.info-desc')?.innerHTML || '';

                    infoModalTitle.innerHTML = title;
                    if (img) {
                        infoModalImg.src = img;
                        infoModalImg.style.display = 'block';
                    } else {
                        infoModalImg.style.display = 'none';
                    }
                    infoModalDesc.innerHTML = desc;
                    infoModal.classList.add('show');
                }
            });
        });

        infoModalClose.addEventListener('click', () => {
            infoModal.classList.remove('show');
        });
        infoModal.addEventListener('click', (e) => {
            if (e.target === infoModal) {
                infoModal.classList.remove('show');
            }
        });
    }

    // === КОПИРОВАНИЕ СТИЛЕЙ/ТЕМ ===
    const copyBtns = document.querySelectorAll('.copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const textToCopy = btn.getAttribute('data-text');
            if (textToCopy) {
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const originalHTML = btn.innerHTML;
                    btn.classList.add('copied');
                    btn.innerHTML = '<svg class="svg-icon" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg> Скопировано';
                    setTimeout(() => {
                        btn.classList.remove('copied');
                        btn.innerHTML = originalHTML;
                    }, 2000);
                });
            }
        });
    });

    // === ФИЛЬТРЫ ТЕГОВ ===
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('article[data-tags]');
    const galleryGrid = document.querySelector('.gallery-grid');
    
    const updateSparseMode = () => {
        if (!galleryGrid) return;
        const visibleCount = Array.from(cards).filter(c => c.style.display !== 'none').length;
        if (visibleCount > 0 && visibleCount <= 4) {
            galleryGrid.classList.add('sparse');
        } else {
            galleryGrid.classList.remove('sparse');
        }
    };
    
    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.getAttribute('data-filter');
                
                cards.forEach(card => {
                    if (filter === 'all') {
                        card.style.display = '';
                    } else {
                        const tags = card.getAttribute('data-tags') || '';
                        if (tags.split(',').map(t => t.trim()).includes(filter)) {
                            card.style.display = '';
                        } else {
                            card.style.display = 'none';
                        }
                    }
                });
                updateSparseMode();
            });
        });
    }

    // === РАНДОМНЫЙ ПРОМПТ ===
    const randomPromptBtn = document.getElementById('randomPromptBtn');
    if (randomPromptBtn) {
        randomPromptBtn.addEventListener('click', () => {
            const visibleCards = Array.from(document.querySelectorAll('.prompt-card')).filter(c => c.style.display !== 'none');
            if (visibleCards.length > 0) {
                const randomCard = visibleCards[Math.floor(Math.random() * visibleCards.length)];
                const img = randomCard.querySelector('.card-img');
                if (img) img.click();
            }
        });
    }

    // === ЛАЙТБОКС ===
    const lightbox = document.getElementById('lightbox');
    if (lightbox) {
        const lightboxImg = document.getElementById('lightboxImg');
        const lightboxClose = document.getElementById('lightboxClose');
        const lightboxPrev = document.getElementById('lightboxPrev');
        const lightboxNext = document.getElementById('lightboxNext');
        const lightboxCopyBtn = document.getElementById('lightboxCopyBtn');

        let currentGallery = [];
        let currentIndex = 0;

        const allCardImgs = document.querySelectorAll('.card-img');
        
        allCardImgs.forEach(img => {
            img.addEventListener('click', () => {
                const parentContainer = img.closest('.carousel-images') || img.parentElement;
                currentGallery = Array.from(parentContainer.querySelectorAll('.card-img'));
                
                // Если это промпты, собираем все видимые промпты
                if (img.closest('.prompt-card')) {
                    const visibleCards = Array.from(document.querySelectorAll('.prompt-card')).filter(card => card.style.display !== 'none');
                    currentGallery = visibleCards.map(c => {
                        // Берем первую картинку в карточке для галереи, или все картинки
                        return c.querySelector('.card-img');
                    }).filter(Boolean);
                }

                currentIndex = currentGallery.indexOf(img);
                if (currentIndex === -1) currentIndex = 0; // fallback

                updateLightboxImage();
                lightbox.classList.add('show');
                document.body.style.overflow = 'hidden';

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
                const currentImg = currentGallery[currentIndex];
                lightboxImg.src = currentImg.src;
                
                if (lightboxCopyBtn) {
                    if (currentImg.hasAttribute('data-prompt')) {
                        lightboxCopyBtn.style.display = 'flex';
                        lightboxCopyBtn.onclick = (e) => {
                            e.stopPropagation();
                            navigator.clipboard.writeText(currentImg.getAttribute('data-prompt')).then(() => {
                                const originalHTML = lightboxCopyBtn.innerHTML;
                                lightboxCopyBtn.classList.add('copied');
                                lightboxCopyBtn.innerHTML = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                                setTimeout(() => {
                                    lightboxCopyBtn.classList.remove('copied');
                                    lightboxCopyBtn.innerHTML = originalHTML;
                                }, 2000);
                            });
                        };
                    } else {
                        lightboxCopyBtn.style.display = 'none';
                    }
                }
            }
        };

        if(lightboxPrev) lightboxPrev.addEventListener('click', (e) => { e.stopPropagation(); currentIndex = (currentIndex > 0) ? currentIndex - 1 : currentGallery.length - 1; updateLightboxImage(); });
        if(lightboxNext) lightboxNext.addEventListener('click', (e) => { e.stopPropagation(); currentIndex = (currentIndex < currentGallery.length - 1) ? currentIndex + 1 : 0; updateLightboxImage(); });

        const closeLightbox = () => {
            lightbox.classList.remove('show');
            document.body.style.overflow = 'auto';
        };

        lightboxClose.addEventListener('click', closeLightbox);
        lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });
        
        document.addEventListener('keydown', (e) => {
            if (!lightbox.classList.contains('show')) return;
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') { currentIndex = (currentIndex > 0) ? currentIndex - 1 : currentGallery.length - 1; updateLightboxImage(); }
            if (e.key === 'ArrowRight') { currentIndex = (currentIndex < currentGallery.length - 1) ? currentIndex + 1 : 0; updateLightboxImage(); }
        });
    }
});
