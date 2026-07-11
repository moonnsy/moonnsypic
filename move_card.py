import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract the card with the donuts safely
# Split by '<article' and find the one with the donut
articles = html.split('<article ')
donut_idx = -1
for i, a in enumerate(articles):
    if 'Two-people-eating-donuts-2K' in a:
        donut_idx = i
        break

if donut_idx != -1:
    # Reconstruct the exact full tag
    # a looks like 'class="glass-card..." ... </article>\n            '
    full_str = '<article ' + articles[donut_idx]
    
    # We only want up to </article>
    end_idx = full_str.find('</article>') + 10
    donut_html = full_str[:end_idx]
    
    # Remove it from html
    html = html.replace(donut_html, '')
    
    # Insert it at the start
    start_str = '<!-- Промпты (Prompts) -->'
    idx = html.find(start_str)
    
    if idx != -1:
        insert_pos = idx + len(start_str)
        html = html[:insert_pos] + '\n            ' + donut_html + html[insert_pos:]
        
        # update cache buster
        html = html.replace('style.css?v=5', 'style.css?v=6')
        html = html.replace('script.js?v=5', 'script.js?v=6')

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print('Successfully moved the card.')
    else:
        print('Could not find start marker.')
else:
    print('Could not find donut article.')
