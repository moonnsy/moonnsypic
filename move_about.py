import os

INDEX_PATH = 'index.html'

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Revert Top Bar Right
top_replacement = """<button id="aboutBtn" class="tg-btn" title="О себе" style="margin-right: 0.5rem; background: rgba(255,255,255,0.05); cursor:pointer;">
                    <svg class="svg-icon" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span class="hide-mobile">О себе</span>
                </button>
                <a href="https://t.me/moonnsypic" class="tg-btn" target="_blank" title="Telegram">"""
top_original = '<a href="https://t.me/moonnsypic" class="tg-btn" target="_blank" title="Telegram">'

if top_replacement in html:
    html = html.replace(top_replacement, top_original)

# 2. Revert Home TG and add About as a category button
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
home_original = """<a href="https://t.me/moonnsypic" class="tg-btn-home" target="_blank">
                <svg class="svg-icon" viewBox="0 0 24 24"><path d="M22 2 11 13"></path><path d="M22 2 15 22 11 13 2 9l20-7z"></path></svg>
                <span>Telegram</span>
            </a>"""

if home_replacement in html:
    html = html.replace(home_replacement, home_original)

# 3. Add About button to home-nav
home_nav_start = '<nav class="home-nav">'
about_nav_btn = """
                <button class="glass-btn" id="aboutBtnHomeNav">
                    <svg class="svg-icon" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span>О себе</span>
                </button>"""

if 'id="aboutBtnHomeNav"' not in html:
    html = html.replace(home_nav_start, home_nav_start + about_nav_btn)

# 4. Add it to the dropdown menu as well
dropdown_start = '<div class="dropdown-content" id="dropdownContent">'
about_dropdown_btn = """
                        <button class="glass-btn" id="aboutBtnDropdown">
                            <svg class="svg-icon" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                            <span>О себе</span>
                        </button>"""

if 'id="aboutBtnDropdown"' not in html:
    html = html.replace(dropdown_start, dropdown_start + about_dropdown_btn)


# bump cache
import re
match = re.search(r'style\.css\?v=(\d+)', html)
if match:
    v = int(match.group(1)) + 1
    html = re.sub(r'style\.css\?v=\d+', f'style.css?v={v}', html)
    html = re.sub(r'script\.js\?v=\d+', f'script.js?v={v}', html)

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
