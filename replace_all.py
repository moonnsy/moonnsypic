import json
import re

with open('out_all.json', 'r', encoding='utf-8') as f:
    new_data = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build new prompts HTML
new_prompts_html = "<!-- Промпты (Prompts) -->\n"
for item in new_data:
    if not isinstance(item['img'], str) or not item['img'].startswith('http'):
        continue
    tags = str(item.get('tags', '')).lower()
    
    t_list = []
    if 'соло' in tags: t_list.append('solo')
    if 'парный' in tags: t_list.append('couple')
    if 'мем' in tags: t_list.append('meme')
    t = ','.join(t_list)
    
    prompt_text = str(item.get('prompt', '')).replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    
    card = f'''            <article class="glass-card prompt-card" data-category="prompt" data-tags="{t}">
                <div class="prompt-img-wrapper">
                    <img src="{item['img']}" alt="Prompt" class="card-img prompt-img" data-prompt="{prompt_text}">
                    <button class="icon-copy-btn copy-prompt-btn" title="Копировать промпт">
                        <svg class="svg-icon" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    </button>
                </div>
            </article>\n'''
    new_prompts_html += card

# Replace old prompts block with new ones
pattern = r'<!-- Промпты \(Prompts\) -->.*?<!-- Расширения -->'
html = re.sub(pattern, new_prompts_html + '            <!-- Расширения -->', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Fixed HTML tags!')
