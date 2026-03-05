"""Remove the old gallery content (lines after </html> of the new structure)."""
with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Everything up to and including the FIRST </html> is correct new content
# Find the first closing html tag
idx = content.find('</html>')
if idx == -1:
    print("No </html> found!")
else:
    clean = content[:idx + len('</html>')]
    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(clean)
    print(f"Cleaned! New size: {len(clean)} chars")
    # Quick verify
    print("Old GB-media still present:", 'GB-media' in clean)
    print("galleryItems still present:", 'galleryItems' in clean)
    print("gl-grid present:", 'gl-grid' in clean)
    print("gl-card count:", clean.count('class="gl-card"'))
