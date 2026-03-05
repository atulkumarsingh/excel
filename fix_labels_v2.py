import os
import re

def fix_css(path):
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Very aggressive regex to remove any font-size: 0 (with optional space, optional px, with !important)
    content = re.sub(r'font-size\s*:\s*0\s*(px|rem|em)?\s*!important\s*;?', '', content)
    # Also without !important if it is 0
    # content = re.sub(r'font-size\s*:\s*0\s*(px|rem|em)?\s*;', '', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_css('assets/css/custom-style.css')
fix_css('assets/css/custom-style.min.css')

# Ensure we force visibility for the form labels
with open('assets/css/custom-style.css', 'a', encoding='utf-8') as f:
    f.write("\n\n/* Force form labels to be visible */\n.form-control-label { font-size: 16px !important; color: #333 !important; display: block !important; margin-bottom: 5px; }\n")

# Update form.html
with open('form.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix textarea placeholder
html = re.sub(r'placeholder="[^"]+"', 'placeholder="Enter your message"', html, count=0) # wait this replaces all placeholders
# Re-read and do specific replacements
html = re.sub(r'placeholder=\"Enter your message here\.\.\.\"', 'placeholder="Enter your message"', html)
html = re.sub(r'placeholder=Enter your message here\.\.\.', 'placeholder="Enter your message"', html)

# Fix labels
html = html.replace('First name', 'First Name')
html = html.replace('Last name', 'Last Name')

with open('form.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done')
