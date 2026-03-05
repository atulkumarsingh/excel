import os, re
html_dir = r'd:\final_code\Excdl Website'
for fname in sorted(os.listdir(html_dir)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(html_dir, fname)
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        c = f.read()
    gq = c.count('GET QUOTE')
    if gq > 0:
        form_links = c.count('href=form.html')
        hash_broken = len(re.findall(r'href\s*=#[^>]*>[^<]*GET QUOTE', c, re.DOTALL))
        status = 'OK' if hash_broken == 0 else 'BROKEN'
        print(f'[{status}] {fname}: {gq} GET QUOTE, {form_links} form.html links, {hash_broken} broken #')
