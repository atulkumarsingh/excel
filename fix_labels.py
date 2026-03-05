import os
import re

def fix_css(path):
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove variations of font-size: 0 !important
    content = re.sub(r'font-size:\s*0(px)?\s*!important;?', '', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_css('assets/css/custom-style.css')
fix_css('assets/css/custom-style.min.css')

# Also update form.html
with open('form.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix placeholder - be defensive with regex
html = re.sub(r'placeholder="Enter your message here\.\.\."', 'placeholder="Enter your message"', html)
html = re.sub(r'placeholder=Enter your message here\.\.\.', 'placeholder="Enter your message"', html) # for unquoted

# Fix capitalization
html = html.replace('>First name<', '>First Name<')
html = html.replace('>Last name<', '>Last Name<')

with open('form.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully cleaned CSS and updated form.html')
