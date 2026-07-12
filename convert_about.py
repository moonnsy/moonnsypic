import os
import re

INDEX_PATH = 'index.html'
SCRIPT_PATH = 'script.js'
STYLE_PATH = 'style.css'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Buttons
html = html.replace('id="aboutBtnHomeNav"', 'data-target="about"')
html = html.replace('id="aboutBtnDropdown"', 'data-target="about"')

# 2. Extract Modal and Remove it
modal_pattern = r'<!-- О себе Modal -->\s*<div class="lightbox" id="aboutModal">[\s\S]*?</div>\s*</div>\s*</div>'
modal_match = re.search(modal_pattern, html)
if modal_match:
    html = html.replace(modal_match.group(0), '')

# 3. Add About Card inside gallery-grid
about_card = """
            <!-- Раздел О себе (About Page) -->
            <article class="glass-card about-page-card" data-category="about" style="display:none;">
                <img src="https://i.postimg.cc/Pqn2nhMK/Woman-on-balcony-at-twilight-202607121717.jpg" alt="About Moonnsy" class="about-page-img">
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
            </article>
"""

# Find closing of gallery-grid
grid_close = '        </div>\n    </main>'
if grid_close in html:
    html = html.replace(grid_close, about_card + '\n' + grid_close)

# 4. Remove Modal JS from script.js
with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
    js = f.read()

js_modal_pattern = r'// === ABOUT MODAL LOGIC ===[\s\S]*?if\(aboutModal\) {\s*aboutModal\.addEventListener\(\'click\', \(e\) => {\s*if\(e\.target === aboutModal\) closeAboutModal\(\);\s*}\);\s*}'
js_match = re.search(js_modal_pattern, js)
if js_match:
    js = js.replace(js_match.group(0), '')

with open(SCRIPT_PATH, 'w', encoding='utf-8') as f:
    f.write(js)

# 5. Update CSS
with open(STYLE_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

if '.about-page-card' not in css:
    css_addition = """
/* === ABOUT PAGE CATEGORY === */
.about-page-card {
    grid-column: 1 / -1; /* Занимает всю ширину сетки */
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    flex-direction: column;
    box-sizing: border-box;
    display: none;
}
.about-page-card.visible {
    display: flex; /* Переопределяем класс visible */
}
.about-page-img {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 2rem;
    max-height: 500px;
    object-fit: cover;
}
"""
    css += css_addition
    with open(STYLE_PATH, 'w', encoding='utf-8') as f:
        f.write(css)

# Bump Cache
match = re.search(r'style\.css\?v=(\d+)', html)
if match:
    v = int(match.group(1)) + 1
    html = re.sub(r'style\.css\?v=\d+', f'style.css?v={v}', html)
    html = re.sub(r'script\.js\?v=\d+', f'script.js?v={v}', html)

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
