with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()
print('Total chars:', len(content))
print('Has old galleryItems:', 'galleryItems' in content)
print('Has old about section:', 'section-header' in content)
print('Has gl-grid:', 'gl-grid' in content)
print('Has gl-lightbox:', 'gl-lightbox' in content)
print('La Perle cards:', content.count('data-prop="la-perle"'))
print('Banyan cards:', content.count('data-prop="banyan"'))
print('Excel Corbett cards:', content.count('data-prop="excel-corbett"'))
print('Mangobloom cards:', content.count('data-prop="mangobloom"'))
print('Total gl-card count:', content.count('class="gl-card"'))
# Check if old content is still there
print('Old GB-media still present:', 'GB-media' in content)
