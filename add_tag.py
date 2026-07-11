import re
with open('index.html', 'r', encoding='utf-8') as f: html = f.read()
pattern = r'(<article[^>]*?data-tags="[^"]*)(">\s*<div class="prompt-img-wrapper">\s*<img src="https://i\.postimg\.cc/wBJXyp4t/photo-2026-07-11-03-49-36\.jpg")'
def repl(m):
    tags = m.group(1)
    if 'meme' not in tags: tags += ',meme'
    return tags + m.group(2)
html = re.sub(pattern, repl, html)
with open('index.html', 'w', encoding='utf-8') as f: f.write(html)
