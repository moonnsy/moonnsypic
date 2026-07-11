import json
import re

with open('out_new.json', 'r', encoding='utf-8') as f:
    new_data = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean up old tags (remove girl)
html = html.replace('data-tags="solo,girl"', 'data-tags="solo"')
html = html.replace('data-tags="girl,solo"', 'data-tags="solo"')
html = html.replace('data-tags="girl"', 'data-tags=""')

# 2. Add custom dropdown & counter
old_header_pattern = r'<div id="promptFilterContainer".*?</div>\s*</div>'
new_header = '''<div id="promptFilterContainer" class="custom-dropdown-container" style="display: none; position: relative;">
                <div id="promptDropdownSelected" class="glass-btn" style="cursor: pointer; padding: 0.5rem 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span id="promptDropdownText">Все промпты</span>
                    <svg class="svg-icon" viewBox="0 0 24 24" width="16" height="16"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </div>
                <div id="promptDropdownOptions" class="glass-panel" style="display: none; position: absolute; top: 110%; right: 0; width: 150px; z-index: 100; padding: 0.5rem; border-radius: 8px; flex-direction: column; gap: 0.2rem; background: var(--glass-bg); border: 1px solid var(--glass-border); backdrop-filter: blur(10px);">
                    <div class="dropdown-option active" data-value="all" style="cursor:pointer; padding: 0.3rem 0.5rem; border-radius: 4px;">Все промпты</div>
                    <div class="dropdown-option" data-value="solo" style="cursor:pointer; padding: 0.3rem 0.5rem; border-radius: 4px;">Соло</div>
                    <div class="dropdown-option" data-value="couple" style="cursor:pointer; padding: 0.3rem 0.5rem; border-radius: 4px;">Парный</div>
                    <div class="dropdown-option" data-value="meme" style="cursor:pointer; padding: 0.3rem 0.5rem; border-radius: 4px;">Мем</div>
                </div>
            </div>
        </div>'''
html = re.sub(old_header_pattern, new_header.strip(), html, flags=re.DOTALL)

# Let's also insert the counter right before the prompt-header
header_div = '<div class="content-header prompt-header"'
counter_html = '''<div id="promptCounterWrapper" style="display:none; width: 100%; text-align: left; margin-bottom: 0.5rem;">
            <span id="promptCounter" style="color: var(--primary); font-family: var(--font-header); font-size: 1.2rem; font-weight: bold; letter-spacing: 1px;">Промптов: 0</span>
        </div>
        <div class="content-header prompt-header"'''
html = html.replace(header_div, counter_html)

# 3. Build new prompts HTML
new_prompts_html = ""
for item in new_data:
    if not isinstance(item['img'], str) or not item['img'].startswith('http'):
        continue
    tags = item['tags'].replace('девушка', '').replace(',', '').strip()
    # Map russian tags to english for data-tags
    t = ''
    if 'соло' in tags.lower(): t = 'solo'
    elif 'парный' in tags.lower(): t = 'couple'
    elif 'мем' in tags.lower(): t = 'meme'
    
    prompt_text = item['prompt'].replace('"', '&quot;')
    
    card = f'''
            <article class="glass-card prompt-card" data-category="prompt" data-tags="{t}">
                <div class="prompt-img-wrapper">
                    <img src="{item['img']}" alt="Prompt" class="card-img prompt-img" data-prompt="{prompt_text}">
                    <button class="icon-copy-btn copy-prompt-btn" title="Копировать промпт">
                        <svg class="svg-icon" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    </button>
                </div>
            </article>'''
    new_prompts_html += card

# 4. Insert before <!-- Расширения -->
html = html.replace('<!-- Расширения -->', new_prompts_html + '\n            <!-- Расширения -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
