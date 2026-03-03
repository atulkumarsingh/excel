import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        modified = content
        
        # 1. Remove empty vrindavan or sardargarh link in resorts dropdown
        modified = re.sub(r'<li[^>]*>\s*<a[^>]*href=\"(vrindavan\.html|www\.sardargarh\.in|)\"[^>]*>.*?</a>\s*</li>', '', modified)
        
        # 2. Fix EXPERIENCES link
        modified = re.sub(r'<a class=\"([^\"]*nav-link scrollto[^\"]*)\" href=\"([^\"]*)\">EXPERIENCES</a>', r'<a class="\1" href="index.html#experiences">EXPERIENCES</a>', modified)
        
        # 3. Fix EVENTS link
        modified = re.sub(r'<a class=\"([^\"]*nav-link scrollto[^\"]*)\" href=\"([^\"]*)\">EVENTS</a>', r'<a class="\1" href="index.html#pre-footer">EVENTS</a>', modified)
        
        # 4. Fix GALLERY link
        modified = re.sub(r'<a class=\"([^\"]*nav-link scrollto[^\"]*)\" href=\"([^\"]*)\">GALLERY</a>', r'<a class="\1" href="gallery.html">GALLERY</a>', modified)
        
        # 5. Fix CONTACT US link
        modified = re.sub(r'<a class=\"([^\"]*nav-link scrollto[^\"]*)\" href=\"([^\"]*)\">CONTACT US</a>', r'<a class="\1" href="contact.html">CONTACT US</a>', modified)

        if content != modified:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(modified)
            print(f'Fixed {f}')
    except Exception as e:
        print(f'Error processing {f}: {e}')
