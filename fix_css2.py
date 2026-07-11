import re

with open('style.css', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Reduce top padding in gallery-wrapper
c = re.sub(r'\.gallery-wrapper\s*\{[^\}]*padding:\s*3rem\s+1\.5rem\s+5rem;', lambda m: m.group(0).replace('3rem', '1rem'), c)

# 2. Add aspect-ratio to .prompt-img
c = re.sub(r'(\.prompt-img\s*\{[^\}]*)height:\s*auto;[^\n]*\n', r'\1aspect-ratio: 3/4;\n    object-fit: cover;\n', c)

# 3. Remove .prompt-filter-btn
c = re.sub(r'/\*\s*Специальная кнопка для фильтра промптов.*?\*/\s*\.prompt-filter-btn\s*\{.*?\.prompt-filter-btn:hover\s*\{[^\}]*\}\s*', '', c, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done fixing style.css')
