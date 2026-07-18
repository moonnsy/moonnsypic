import os
import re

OLD_DIR = os.path.abspath(os.path.dirname(__file__))
OLD_INDEX = os.path.join(OLD_DIR, 'source_data.html')
NEW_DIR = OLD_DIR

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moonnsy — {TITLE}</title>
    <link rel="icon" type="image/png" href="sprite_0004.png">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&family=VT323&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script>
        const savedTheme = localStorage.getItem('moonnsy-theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
    </script>
</head>
<body>
    <div class="top-menu">
        <a href="javascript:history.back()"><svg class="menu-icon" viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg> Back</a>
        <a href="index.html"><svg class="menu-icon" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg> Home</a>
        <a href="prompts.html"><svg class="menu-icon" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg> Prompts</a>
        <a href="styles.html"><svg class="menu-icon" viewBox="0 0 24 24"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg> Styles</a>
        <a href="themes.html"><svg class="menu-icon" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/></svg> Themes</a>
        <a href="extensions.html"><svg class="menu-icon" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg> Extensions</a>
        <a href="about.html"><svg class="menu-icon" viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/></svg> About</a>
        <a href="https://t.me/moonnsypic" target="_blank" title="Telegram"><svg class="menu-icon" viewBox="0 0 24 24"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/></svg></a>
    </div>
    <div class="container">
        <div class="page-header">
            <h1>{HEADER}</h1>
        </div>
        {FILTERS}
        <div class="standard-grid">
            {CONTENT}
        </div>
    </div>
    
    <!-- Lightbox -->
    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightboxClose">x</button>
        <button class="lightbox-nav lightbox-prev" id="lightboxPrev">&lt;</button>
        <button class="lightbox-nav lightbox-next" id="lightboxNext">&gt;</button>
        <div class="lightbox-content">
            <img src="" alt="Fullscreen" class="lightbox-img" id="lightboxImg">
            <button class="lightbox-copy-btn" id="lightboxCopyBtn" style="display:none;" title="Скопировать промпт">
                <svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            </button>
        </div>
    </div>
    
    <!-- Info Modal -->
    <div id="infoModal" class="lightbox">
        <div class="lightbox-content" style="background: var(--window-bg); border: 2px solid var(--window-border); border-radius: 8px; max-width: 600px; padding: 20px; text-align: left; position: relative; width: 90vw;">
            <button class="lightbox-close" id="infoModalClose">x</button>
            <img id="infoModalImg" src="" alt="Cover" style="width: 100%; border-radius: 4px; margin-bottom: 15px; display: none;">
            <h2 id="infoModalTitle" style="color: var(--text-main); font-family: var(--font-title); margin-bottom: 10px;">Title</h2>
            <div id="infoModalDesc" style="color: var(--text-main); font-size: 14px; line-height: 1.5; max-height: 50vh; overflow-y: auto; padding-right: 10px;">Description</div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>"""

def parse_cards():
    with open(OLD_INDEX, 'r', encoding='utf-8') as f:
        html = f.read()

    # Извлекаем все <article>
    # Используем нежадный поиск до закрывающего </article>
    pattern = r'<article[^>]*?class="[^"]*glass-card[^"]*"[^>]*?data-category="([^"]*)"(?:[^>]*?data-tags="([^"]*)")?[^>]*>(.*?)</article>'
    matches = re.finditer(pattern, html, re.DOTALL)
    
    cards_by_category = {
        'prompt': [],
        'style': [],
        'theme': [],
        'extension': [],
        'about': [],
        'recolors': []
    }
    
    STAR_ICON = '<svg class="title-icon" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87L18.18 22 12 18.56 5.82 22 7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
    
    CATEGORY_LABELS = {
        'prompt': 'PROMPT',
        'style': 'STYLE',
        'theme': 'THEME',
        'extension': 'EXTENSION',
        'about': 'ABOUT',
        'recolors': 'RECOLORS',
    }

    for match in matches:
        category = match.group(1)
        tags = match.group(2) or ''
        inner_html = match.group(3)
        
        # Remove the redundant badge from inside the card
        inner_html = re.sub(r'<span class="badge">.*?</span>\s*', '', inner_html, flags=re.DOTALL)
        
        if category == 'extension':
            import hashlib
            title_match = re.search(r'<div class="info-title">(.*?)</div>', inner_html, re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
                slug = hashlib.md5(title.encode()).hexdigest()[:8]
                
                img_match = re.search(r'<div class="info-img">(.*?)</div>', inner_html, re.DOTALL)
                desc_match = re.search(r'<div class="info-desc">(.*?)</div>\s*</div>', inner_html, re.DOTALL)
                
                if desc_match:
                    img_url = img_match.group(1).strip() if img_match else ''
                    desc_html = desc_match.group(1).strip()
                    
                    ext_page_content = f'''
                    <div class="about-container" style="max-width: 800px; margin: 0 auto; width: 100%;">
                        <article class="retro-window about-card" data-tags="{tags}" style="display: block; width: 100%; box-sizing: border-box;">
                            <div class="window-titlebar">
                                <div class="window-title">{STAR_ICON} {title}</div>
                                <div class="window-controls">
                                    <div class="control-btn control-min"></div>
                                    <div class="control-btn control-max"></div>
                                    <div class="control-btn control-close"></div>
                                </div>
                            </div>
                            <div class="window-content">
                                <img src="{img_url}" alt="{title}" class="about-page-img" style="margin-bottom: 20px;">
                                <div class="about-text">
                                    {desc_html}
                                </div>
                            </div>
                        </article>
                    </div>
                    '''
                    
                    ext_page = TEMPLATE.format(
                        TITLE=title,
                        HEADER=title.upper(),
                        FILTERS="",
                        CONTENT=ext_page_content
                    ).replace('<div class="standard-grid">', '<div>')
                    
                    with open(os.path.join(NEW_DIR, f'ext_{slug}.html'), 'w', encoding='utf-8') as ext_f:
                        ext_f.write(ext_page)
                    
                    # Modify inner_html to link to the new page and remove hidden data
                    inner_html = re.sub(r'<!-- Скрытые данные.*?</div>\s*</div>', '', inner_html, flags=re.DOTALL)
                    inner_html = re.sub(r'<button class="view-btn info-btn">.*?<span>Подробнее</span>\s*</button>', 
                                        f'<a href="ext_{slug}.html" class="view-btn" style="text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px;">'
                                        f'<svg class="svg-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>'
                                        f'<span>Подробнее</span></a>', inner_html, flags=re.DOTALL)
        
        label = CATEGORY_LABELS.get(category, category.upper())
        
        new_card = f'''
        <article class="retro-window {category}-card" data-tags="{tags}">
            <div class="window-titlebar">
                <div class="window-title">{STAR_ICON} {label}</div>
                <div class="window-controls">
                    <div class="control-btn control-min"></div>
                    <div class="control-btn control-max"></div>
                    <div class="control-btn control-close"></div>
                </div>
            </div>
            <div class="window-content">
                {inner_html}
            </div>
        </article>
        '''
        
        if category in cards_by_category:
            cards_by_category[category].append(new_card)
        else:
            cards_by_category[category] = [new_card]
            
    return cards_by_category

def build_site():
    cards = parse_cards()
    
    # 1. Prompts
    filters_html = '''
    <div class="filters">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="solo">Solo</button>
        <button class="filter-btn" data-filter="couple">Couple</button>
        <button class="filter-btn" data-filter="meme">Meme</button>
        <button class="filter-btn" data-filter="gacha">Gacha</button>
        <button id="randomPromptBtn" class="random-btn">
            <svg class="menu-icon" viewBox="0 0 24 24" style="stroke: currentColor; width: 16px; height: 16px; margin-right: 4px;">
                <path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/>
            </svg> Random
        </button>
    </div>
    '''
    prompts_page = TEMPLATE.format(
        TITLE="Prompts",
        HEADER="PROMPTS",
        FILTERS=filters_html,
        CONTENT="\n".join(cards.get('prompt', []))
    ).replace('<div class="standard-grid">', '<div class="gallery-grid">')
    with open(os.path.join(NEW_DIR, 'prompts.html'), 'w', encoding='utf-8') as f:
        f.write(prompts_page)
        
    # 2. Styles
    styles_page = TEMPLATE.format(
        TITLE="Styles",
        HEADER="STYLES",
        FILTERS="",
        CONTENT="\n".join(cards.get('style', []))
    )
    with open(os.path.join(NEW_DIR, 'styles.html'), 'w', encoding='utf-8') as f:
        f.write(styles_page)
        
    # 3. Themes
    themes_page = TEMPLATE.format(
        TITLE="Themes",
        HEADER="THEMES",
        FILTERS="",
        CONTENT="\n".join(cards.get('theme', []))
    )
    with open(os.path.join(NEW_DIR, 'themes.html'), 'w', encoding='utf-8') as f:
        f.write(themes_page)
        
    # 4. Extensions
    ext_page = TEMPLATE.format(
        TITLE="Extensions",
        HEADER="EXTENSIONS",
        FILTERS="",
        CONTENT="\n".join(cards.get('extension', []))
    )
    with open(os.path.join(NEW_DIR, 'extensions.html'), 'w', encoding='utf-8') as f:
        f.write(ext_page)
        
    # 5. About
    about_page = TEMPLATE.format(
        TITLE="About",
        HEADER="ABOUT ME",
        FILTERS="",
        CONTENT="\n".join(cards.get('about', []))
    ).replace('<div class="standard-grid">', '<div class="about-container" style="max-width: 800px; margin: 0 auto; width: 100%;">').replace('class="retro-window about-card"', 'class="retro-window about-card" style="display: block; width: 100%; box-sizing: border-box;"')
    
    with open(os.path.join(NEW_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(about_page)
        
    # 6. Index (Home)
    # 6. Index (Home)
    home_content = '''
    <div class="about-container" style="max-width: 700px; margin: 40px auto; width: 100%;">
        <article class="retro-window" style="width: 100%; display: block; box-sizing: border-box;">
            <div class="window-titlebar">
                <div class="window-title"><svg class="title-icon" viewBox="0 0 24 24"><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg> DIRECTORY</div>
                <div style="display: flex; gap: 12px; align-items: center;">
                    <button id="themeToggleBtn" style="background:none; border:none; cursor:pointer; color: var(--accent); padding: 0; display: flex; align-items: center; justify-content: center;" title="Переключить тему">
                        <svg viewBox="0 0 24 24" class="theme-icon" style="width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
                    </button>
                    <div class="window-controls">
                        <div class="control-btn control-min"></div>
                        <div class="control-btn control-max"></div>
                        <div class="control-btn control-close"></div>
                    </div>
                </div>
            </div>
            <div class="window-content" style="padding: 35px 30px; text-align: center; box-sizing: border-box;">
                <img src="https://i.postimg.cc/fbKpTmzm/Woman-with-piercings-and-decals-202607181859.jpg" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%; border: 4px solid var(--window-border); outline: 2px solid var(--accent); outline-offset: 4px; margin: 0 auto 25px auto; display: block;">
                <h2 style="font-family: var(--font-title); color: var(--accent); font-size: 2rem; margin: 0 0 25px 0;">Moonnsy</h2>
                
                <div style="display: flex; flex-direction: column; gap: 12px; width: 100%; margin: 0 auto;">
                    <a href="prompts.html" class="action-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                        Prompts
                    </a>
                    <a href="styles.html" class="action-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
                        Styles
                    </a>
                    <a href="themes.html" class="action-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/></svg>
                        Themes
                    </a>
                    <a href="extensions.html" class="action-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
                        Extensions
                    </a>
                    <a href="about.html" class="action-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7" r="4"/><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/></svg>
                        About
                    </a>
                    <a href="https://t.me/moonnsypic" target="_blank" class="action-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/></svg>
                        Telegram
                    </a>
                </div>
            </div>
        </article>
    </div>
    '''
    
    # Hide the top menu entirely on the index page
    index_page = TEMPLATE.format(
        TITLE="Home",
        HEADER="",
        FILTERS="",
        CONTENT=home_content
    ).replace('<div class="top-menu">', '<div class="top-menu" style="display: none;">').replace('<div class="standard-grid">', '<div>')
    
    # Also remove the page-header H1 empty block
    index_page = index_page.replace('<div class="page-header">\n            <h1></h1>\n        </div>', '')
    with open(os.path.join(NEW_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_page)
        
    # 7. Recolors
    recolors_page = TEMPLATE.format(
        TITLE="Recolors",
        HEADER="RECOLORS",
        FILTERS="",
        CONTENT="\n".join(cards.get('recolors', []))
    )
    with open(os.path.join(NEW_DIR, 'recolors.html'), 'w', encoding='utf-8') as f:
        f.write(recolors_page)

if __name__ == '__main__':
    build_site()
    print("Migration complete!")
