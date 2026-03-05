"""
Fix all GET QUOTE CTAs to link to form.html
Replaces:  href=# ... GET QUOTE   with href=form.html
Handles both href=# and href="./form.html" variants already correct
"""
import os, re

html_dir = r'd:\final_code\Excdl Website'
changed_files = []

for fname in os.listdir(html_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(html_dir, fname)
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content

    # Pattern: an <a> tag with href=# (or href="#") that contains GET QUOTE text
    # We look for the full anchor tag containing GET QUOTE and replace href=# with href=form.html
    # This handles: <a class="text-end btn-ind" href=#> ... GET QUOTE ... </a>
    # and:          <a class="text-end btn-ind" href="#">  ... GET QUOTE ... </a>

    # Replace href=# on lines/segments that contain GET QUOTE within close proximity
    # Strategy: find all <a> tags where href is # AND the tag content contains GET QUOTE
    def fix_get_quote_links(html):
        # Match <a...href=#...>content</a> or <a...href="#">content</a> where content has GET QUOTE
        pattern = r'(<a\b[^>]*\bhref\s*=\s*["\']?#["\']?[^>]*>)((?:(?!</a>).)*?GET QUOTE(?:(?!</a>).)*?)(</a>)'
        def replacer(m):
            open_tag, inner, close_tag = m.group(1), m.group(2), m.group(3)
            # Replace href=# or href="#" with href=form.html
            open_tag = re.sub(r'\bhref\s*=\s*["\']?#["\']?', 'href=form.html', open_tag)
            return open_tag + inner + close_tag
        return re.sub(pattern, replacer, html, flags=re.DOTALL | re.IGNORECASE)

    content = fix_get_quote_links(content)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        # Count changes
        orig_hashes = original.count('href=#')
        new_hashes = content.count('href=#')
        changed_files.append((fname, orig_hashes - new_hashes))
        print(f'✓ Fixed {fname}: {orig_hashes - new_hashes} GET QUOTE link(s) updated')
    else:
        # Check if it already has form.html links for GET QUOTE
        if 'GET QUOTE' in content:
            print(f'  {fname}: GET QUOTE already links correctly (no # found)')

print()
print(f'Total files modified: {len(changed_files)}')
print('Done!')
