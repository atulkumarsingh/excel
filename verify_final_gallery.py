with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()
with open('assets/css/gallery.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('=== gallery.html ===')
print(f'File size: {len(c)} chars')
print(f'gl-tile-stack remaining: {c.count("gl-tile-stack")}')
print(f'Featured tiles (span 2 rows): {c.count("class=\"gl-tile featured\"")}')
print(f'Regular tiles: {c.count("class=\"gl-tile\"")}')
print(f'Section headers: {c.count("gl-section-header")}')

print()
print('=== gallery.css ===')
print(f'grid-auto-rows present: {"grid-auto-rows" in css}')
print(f'span 2 row: {"span 2" in css}')
print(f'aspect-ratio on tiles: {"aspect-ratio: 4/3" in css or "aspect-ratio: 16/9" in css}')
print(f'Mobile 160px rows: {"160px" in css}')
print(f'Tablet 200px rows: {"200px" in css}')
print(f'Desktop 240px rows: {"240px" in css}')
