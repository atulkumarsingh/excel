with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()
with open('assets/css/gallery.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('gallery.html size:', len(c), 'chars')
print('Section headers:', c.count('gl-section-header'))
print('Featured tiles:', c.count('class="gl-tile featured"'))
print('Stacked groups:', c.count('class="gl-tile-stack"'))
print('Gold section dividers:', c.count('gl-section-divider'))
print('Section titles:', c.count('gl-section-title'))
print('Has JS controller:', 'applyFilters' in c)
print('Mobile 2-col CSS:', 'repeat(2, 1fr)' in css)
print('Mobile 900px breakpoint:', '900px' in css)
print('Mobile 600px breakpoint:', '600px' in css)
