import re, os

pages = ['la-perle.html','banyan-retreat.html','excel-corbett.html','excel-nainital.html','excel-bhimtal.html','mangobloom-resort.html']
print('=== FOOTER ADDRESSES ===')
for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'CONTACT US</h6>(.*?)</div></div>', c, re.DOTALL)
    if m:
        h6 = re.search(r'<h6>(.*?)</h6>', m.group(1))
        addr = bool(re.search(r'Uttarakhand|Nainital', m.group(1)))
        name = h6.group(1) if h6 else '??'
        print(f'  {page}: {name} | addr found: {addr}')
    else:
        print(f'  {page}: [footer NOT found]')

print()
print('=== NAV DROPDOWN (la-perle.html) ===')
with open('la-perle.html', 'r', encoding='utf-8') as f:
    c = f.read()
links = re.findall(r'href=([\w\-]+\.html)>', c[:2500])
for l in links:
    exists = 'OK' if os.path.exists(l) else '404'
    print(f'  [{exists}] {l}')

print()
print('=== ALL HTML FILES ===')
for h in sorted(f for f in os.listdir('.') if f.endswith('.html')):
    print(f'  {h} ({os.path.getsize(h)} bytes)')
