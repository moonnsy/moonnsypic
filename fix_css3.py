import re

with open('style.css', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Revert .prompt-img to height: auto
c = re.sub(r'aspect-ratio:\s*3/4;\s*\n\s*object-fit:\s*cover;\s*\n', r'height: auto;\n    ', c)

# 2. Add back the masonry column logic for prompts
masonry_css = '''
/* === ИСКЛЮЧЕНИЕ ДЛЯ ПРОМПТОВ (Pinterest-стиль) === */
body[data-active-category="prompt"] .gallery-grid {
    display: block; /* Отключаем Grid */
    column-count: 3;
    column-gap: 1.5rem;
}
@media (max-width: 1024px) {
    body[data-active-category="prompt"] .gallery-grid { column-count: 2; }
}
@media (max-width: 600px) {
    body[data-active-category="prompt"] .gallery-grid { column-count: 1; }
}

.glass-card[data-category="prompt"] {
    break-inside: avoid; /* Защита от разрыва внутри колонок */
    margin-bottom: 1.5rem;
}
'''
if 'body[data-active-category="prompt"] .gallery-grid' not in c:
    c = c.replace('.glass-card[data-category="prompt"] {\n    margin-bottom: 0;\n}', '')
    c += '\n' + masonry_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(c)
print('Restored Pinterest style')
