import os

INDEX_PATH = 'index.html'
SCRIPT_PATH = 'script.js'
STYLE_PATH = 'style.css'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Home Page Telegram Button
home_tg = """<a href="https://t.me/moonnsypic" class="tg-btn-home" target="_blank">
                <svg class="svg-icon" viewBox="0 0 24 24"><path d="M22 2 11 13"></path><path d="M22 2 15 22 11 13 2 9l20-7z"></path></svg>
                <span>Telegram</span>
            </a>"""
home_replacement = """<div style="display:flex; gap:1rem; align-items:center; justify-content:center; margin-bottom:2rem; flex-wrap:wrap;">
                <button id="aboutBtnHome" class="tg-btn-home" style="margin-bottom:0; cursor:pointer;">
                    <svg class="svg-icon" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span>О себе</span>
                </button>
                <a href="https://t.me/moonnsypic" class="tg-btn-home" target="_blank" style="margin-bottom:0;">
                    <svg class="svg-icon" viewBox="0 0 24 24"><path d="M22 2 11 13"></path><path d="M22 2 15 22 11 13 2 9l20-7z"></path></svg>
                    <span>Telegram</span>
                </a>
            </div>"""

if home_tg in html:
    html = html.replace(home_tg, home_replacement)

# 2. Update Top Bar Telegram Button
top_tg = '<a href="https://t.me/moonnsypic" class="tg-btn" target="_blank" title="Telegram">'
top_replacement = """<button id="aboutBtn" class="tg-btn" title="О себе" style="margin-right: 0.5rem; background: rgba(255,255,255,0.05); cursor:pointer;">
                    <svg class="svg-icon" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span class="hide-mobile">О себе</span>
                </button>
                <a href="https://t.me/moonnsypic" class="tg-btn" target="_blank" title="Telegram">"""

if top_tg in html:
    html = html.replace(top_tg, top_replacement)

# 3. Inject Modal at the end of body
about_modal = """
    <!-- О себе Modal -->
    <div class="lightbox" id="aboutModal">
        <div class="info-modal-content about-modal-content" style="max-height:85dvh; overflow-y:auto; padding:2rem; box-sizing:border-box;">
            <button id="aboutModalClose" class="info-modal-close" style="position:absolute; top:1rem; right:1rem; background:rgba(0,0,0,0.5); border-radius:50%; width:36px; height:36px; border:none; color:white; cursor:pointer; display:flex; justify-content:center; align-items:center; z-index:10;">
                <svg class="svg-icon" viewBox="0 0 24 24" style="width:18px;height:18px;"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
            <img src="https://i.postimg.cc/Pqn2nhMK/Woman-on-balcony-at-twilight-202607121717.jpg" alt="About Moonnsy" class="info-modal-img" style="width:100%; border-radius:12px; margin-bottom:1.5rem; max-height:400px; object-fit:cover;">
            <div class="info-modal-text">
                <h2 style="margin-top:0; color:var(--primary); font-family:var(--font-heading); font-size:2rem; margin-bottom:1rem;">О себе</h2>
                <div class="about-text">
                    <p>Всем привет! ✨</p>
                    <p>Меня зовут Ксюша или просто Мунси, как угодно. Я люблю красивые картиночки, всякие приколы, ролевые в таверне и делать всё, лишь бы не работать (но всё равно приходится ахахах)</p>
                    <p>Здесь собрано всё что я делала для картиночек и самой таверны:</p>
                    <ul>
                        <li>Расширения для SillyTavern</li>
                        <li>Промпты для генерации картинок</li>
                        <li>Стили для генерации картинок на модели Nano Banana 2 Lite</li>
                        <li>Темы для SillyTavern</li>
                        <li>Возможно в будущем что-то ещё добавится, обновится и вообще я много чего хочу сделать (может гайды.... кто знает)</li>
                    </ul>
                    <p>Чучуть деталей:</p>
                    <ul>
                        <li>Картинки и видео я генерирю в <a href="https://labs.google/flow/about" target="_blank">Google Flow</a>. Поподробнее о нём можно почитать в <a href="https://t.me/cadis_ai/11" target="_blank">посте</a> моей любимой Кадис.</li>
                        <li>Стили для картинок: Я использую стили либо свои с этого сайта, либо беру стили с <a href="https://ann22cadis.github.io/cadis-ai" target="_blank">сайта</a> Кадис, либо использую немного изменённый стиль от <a href="https://t.me/sillykamoi" target="_blank">Камои</a>:
                            <details style="margin-top:0.5rem; background:rgba(255,255,255,0.05); padding:0.5rem; border-radius:6px; cursor:pointer;">
                                <summary style="font-weight:bold; color:var(--primary);">Показать стиль</summary>
                                <div style="margin-top:0.5rem; font-size:0.85rem; font-family:monospace; color:#ccc; line-height:1.4;">Semi-realistic digital painting, WLOP inspired. Natural balanced color palette — neutral skin tones with healthy warmth, no color cast. Gentle shadows with natural color, not tinted blue or green. Anatomically correct hands and proportions. Match the rendering technique, line quality, texture, and ornamental details from the reference image. Avoid: stubble, beard, exaggerated expressions, uncanny valley, bad anatomy, watermark, text, blurry</div>
                            </details>
                            <br>Референс очень влияет на результат картинки, помните! На результат влияет и настроение модели и загруженность серверов гугл (ง ื▿ ื)ว
                        </li>
                        <li>По любым багам, вопросам и идеям вы всегда можете обратиться в комментариях, чатике канала или, если стесняетесь, напишите просто в ЛС самого канала.</li>
                    </ul>
                    <p>Поддержать меня вы можете любым способом:</p>
                    <ul>
                        <li>Подписаться на мой <a href="https://t.me/moonnsypic" target="_blank">Телеграм канал</a></li>
                        <li>Ставить реакции на постики, меня они очень радуют, а ещё это бесплатново!! То же самое и с комментариями! Люблю когда вы делитесь своими получившимися картиночками!</li>
                        <li>Дать <a href="https://t.me/boost/moonnsypic" target="_blank">бусты</a> каналу для красивых реакций и оформления</li>
                        <li>Самый хардкорный и неловкий, всё по личному желанию – можно кинуть мини <a href="https://boosty.to/moonnsypic/donate" target="_blank">донатик</a> на бусти!</li>
                    </ul>
                    <p style="margin-top:2rem; font-weight:bold; color:var(--primary); font-size:1.1rem; text-align:center;">Спасибо за внимание, вы чудо! 💖</p>
                </div>
            </div>
        </div>
    </div>
"""

if 'id="aboutModal"' not in html:
    # insert before the first script tag
    script_idx = html.rfind('<script src="script.js')
    if script_idx != -1:
        html = html[:script_idx] + about_modal + '\n    ' + html[script_idx:]

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

# 4. Add JS to script.js
with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
    js = f.read()

if 'aboutBtnHome' not in js:
    js_addition = """
    // === ABOUT MODAL LOGIC ===
    const aboutBtn = document.getElementById('aboutBtn');
    const aboutBtnHome = document.getElementById('aboutBtnHome');
    const aboutModal = document.getElementById('aboutModal');
    const aboutModalClose = document.getElementById('aboutModalClose');

    function openAboutModal() {
        if(aboutModal) {
            aboutModal.style.display = 'flex';
            setTimeout(() => aboutModal.classList.add('show'), 10);
            document.body.style.overflow = 'hidden';
        }
    }

    function closeAboutModal() {
        if(aboutModal) {
            aboutModal.classList.remove('show');
            setTimeout(() => {
                aboutModal.style.display = 'none';
                document.body.style.overflow = '';
            }, 300);
        }
    }

    if(aboutBtn) aboutBtn.addEventListener('click', openAboutModal);
    if(aboutBtnHome) aboutBtnHome.addEventListener('click', openAboutModal);
    if(aboutModalClose) aboutModalClose.addEventListener('click', closeAboutModal);
    
    // Close on click outside
    if(aboutModal) {
        aboutModal.addEventListener('click', (e) => {
            if(e.target === aboutModal) closeAboutModal();
        });
    }
"""
    js += js_addition
    with open(SCRIPT_PATH, 'w', encoding='utf-8') as f:
        f.write(js)

# 5. Add CSS to style.css
with open(STYLE_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

if '.about-text' not in css:
    css_addition = """
/* === ABOUT MODAL === */
.about-modal-content {
    max-width: 700px;
    background: #0a0e17;
    border: 1px solid var(--glass-border);
}
.about-text {
    font-family: var(--font-body);
    line-height: 1.6;
    color: var(--text-main);
    font-size: 0.95rem;
}
.about-text p { margin-bottom: 1rem; }
.about-text ul { margin-left: 1.5rem; margin-bottom: 1rem; }
.about-text li { margin-bottom: 0.5rem; }
.about-text a { color: var(--primary); text-decoration: none; border-bottom: 1px dashed var(--primary); transition: 0.3s; font-weight: 500; }
.about-text a:hover { color: #fff; border-bottom-color: #fff; }
"""
    css += css_addition
    with open(STYLE_PATH, 'w', encoding='utf-8') as f:
        f.write(css)

# bump cache
import re
match = re.search(r'style\.css\?v=(\d+)', html)
if match:
    v = int(match.group(1)) + 1
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'style\.css\?v=\d+', f'style.css?v={v}', html)
    html = re.sub(r'script\.js\?v=\d+', f'script.js?v={v}', html)
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
