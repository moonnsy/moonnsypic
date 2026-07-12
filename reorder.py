import re

INDEX_PATH = 'index.html'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Desired order
desired_order = ['about', 'prompt', 'extension', 'theme', 'style']

def reorder_buttons(html_content, container_start_tag, container_end_tag):
    # Find the container
    start_idx = html_content.find(container_start_tag)
    if start_idx == -1: return html_content
    
    end_idx = html_content.find(container_end_tag, start_idx)
    if end_idx == -1: return html_content
    
    container_inner = html_content[start_idx + len(container_start_tag):end_idx]
    
    # Extract buttons
    buttons = {}
    btn_pattern = r'<button class="glass-btn" data-target="([^"]+)">[\s\S]*?</button>'
    for match in re.finditer(btn_pattern, container_inner):
        target = match.group(1)
        buttons[target] = match.group(0)
    
    # Rebuild inner content in desired order
    new_inner = "\n"
    for target in desired_order:
        if target in buttons:
            # We add some spacing for formatting
            new_inner += "                  " + buttons[target].replace("\n", "\n                  ") + "\n"
            
    # Remove the extra spaces added to the very end
    new_inner = new_inner.rstrip() + "\n              "
    
    # Replace in html
    return html_content[:start_idx + len(container_start_tag)] + new_inner + html_content[end_idx:]

# 1. Reorder .home-nav
html = reorder_buttons(html, '<nav class="home-nav">', '</nav>')

# 2. Reorder dropdownContent
html = reorder_buttons(html, '<div class="dropdown-content" id="dropdownContent">', '</div>')

# Bump Cache
match = re.search(r'style\.css\?v=(\d+)', html)
if match:
    v = int(match.group(1)) + 1
    html = re.sub(r'style\.css\?v=\d+', f'style.css?v={v}', html)
    html = re.sub(r'script\.js\?v=\d+', f'script.js?v={v}', html)

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
