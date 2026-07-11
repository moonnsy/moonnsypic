import re

with open('style.css', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'body\[data-active-category="prompt"\] \.gallery-grid \{.*?margin-bottom: 1\.5rem;\s*\}'
c = re.sub(pattern, '.glass-card[data-category="prompt"] {\n    margin-bottom: 0;\n}', c, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done')
