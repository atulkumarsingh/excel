"""
Fix all hotel pages:
1. Update nav dropdown in ALL HTML pages to show all 6 hotels with correct links
2. Fix footer addresses per hotel page
3. Create mangobloom-resort.html by cloning banyan-retreat.html
4. Fix any broken links (Jimcorbett.html -> jim-corbett.html, 1mangobloom, etc.)
"""
import os
import re
import shutil

# ─── CORRECT NAV DROPDOWN FOR ALL PAGES ──────────────────────────────────────
CORRECT_NAV_DROPDOWN = """<ul><li><a href=la-perle.html>La Perle River Resort, Jim Corbett</a><li><a href=banyan-retreat.html>The Banyan Retreat, Jim Corbett</a><li><a href=excel-corbett.html>Excel Hotels &amp; Resorts, Jim Corbett</a><li><a href=excel-nainital.html>Excel Hotels &amp; Resorts, Nainital</a><li><a href=excel-bhimtal.html>Excel Hotels &amp; Resorts, Bhimtal</a><li><a href=mangobloom-resort.html>Mangobloom River Resort, Jim Corbett</a></ul>"""

# ─── FOOTER ADDRESSES PER PAGE ────────────────────────────────────────────────
FOOTER_ADDRESSES = {
    'la-perle.html': {
        'name': 'LA PERLE RIVER RESORT',
        'addr': 'Dhikuli, Village Lodhuachaur,<br>Ramnagar, Uttarakhand – 244715',
    },
    'banyan-retreat.html': {
        'name': 'THE BANYAN RETREAT',
        'addr': 'Choi, Santosh Pur, Near Hanuman Dham,<br>Ramnagar, Uttarakhand – 263136',
    },
    'excel-corbett.html': {
        'name': 'EXCEL HOTELS &amp; RESORTS, JIM CORBETT',
        'addr': 'Pawalgarh Road, Kotabagh,<br>Ramnagar, Uttarakhand – 263136',
    },
    'excel-nainital.html': {
        'name': 'EXCEL HOTELS &amp; RESORTS, NAINITAL',
        'addr': 'Mall Road, Library, Tallital,<br>Nainital, Uttarakhand – 263002',
    },
    'excel-bhimtal.html': {
        'name': 'EXCEL HOTELS &amp; RESORTS, BHIMTAL',
        'addr': 'Mehragaon, Bhowali-Bhimtal Road,<br>Bhimtal, Uttarakhand – 263136',
    },
    'mangobloom-resort.html': {
        'name': 'MANGOBLOOM RIVER RESORT',
        'addr': 'Mohaan, Ranikhet Road,<br>Ramnagar, Uttarakhand – 244715',
    },
}

# Build the hotel footer contact block
def build_hotel_footer_contact(name, addr):
    return f"""<h6>{name}</h6><p class=m-0>{addr}</p><p class=m-0><a class="font-Brandon color-dgrey f-s-16" href=tel:+919211301999>+91 9211301999</a></p><p class=m-0><a class="font-Brandon color-dgrey f-s-16" href=mailto:resv@excelhotelandresort.com>resv@excelhotelandresort.com</a></p>"""

def fix_nav_dropdown(content):
    """Replace whatever dropdown ul is inside the RESORTS dropdown with the correct one."""
    # Pattern: matches the dropdown UL right after RESORTS link
    # The dropdown UL follows <span>RESORTS</span>...<ul>...</ul>
    pattern = r'(<span>RESORTS</span>\s*<i[^>]*></i></a>\s*)<ul>.*?</ul>'
    replacement = r'\1' + CORRECT_NAV_DROPDOWN
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content == content:
        # Try alternative pattern (without closing i tag variant)
        pattern2 = r'(RESORTS[^<]*<[^>]*>[^<]*</[^>]*>[^<]*</a>[^<]*)<ul>.*?</ul>'
        new_content = re.sub(pattern2, replacement, content, flags=re.DOTALL)
    return new_content

def fix_footer_contact(content, name, addr):
    """Replace the contact block in the footer with hotel-specific address."""
    hotel_block = build_hotel_footer_contact(name, addr)
    # Replace content of the 3rd col-md-4 div (the contact column)
    # Pattern: The quicklinks div with h6>CONTACT US heading
    pattern = r'(<div class=quicklinks><h6>CONTACT US</h6>).*?(</div></div>)'
    replacement = r'\1' + hotel_block + r'\2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    return new_content

# ─── STEP 1: Create mangobloom-resort.html from banyan-retreat.html ───────────
print("Creating mangobloom-resort.html...")
with open('banyan-retreat.html', 'r', encoding='utf-8') as f:
    mangobloom_content = f.read()

# Update hotel name in about section
mangobloom_content = mangobloom_content.replace(
    'THE BANYAN RETREAT JIM CORBETT',
    'MANGOBLOOM RIVER RESORT, JIM CORBETT'
)
mangobloom_content = mangobloom_content.replace(
    'BANYAN RETREAT JIM CORBETT',
    'MANGOBLOOM RIVER RESORT, JIM CORBETT'
)
# Update any title/heading references
mangobloom_content = re.sub(
    r'The Banyan Retreat[,]? Jim Corbett',
    'Mangobloom River Resort, Jim Corbett',
    mangobloom_content,
    flags=re.IGNORECASE
)
mangobloom_content = re.sub(
    r'THE BANYAN RETREAT[,]? JIM CORBETT',
    'MANGOBLOOM RIVER RESORT, JIM CORBETT',
    mangobloom_content
)
# hero class - change from hero2 to hero6 (if exists)
mangobloom_content = mangobloom_content.replace('class="hero2 ', 'class="hero6 ')

print("Writing mangobloom-resort.html...")
with open('mangobloom-resort.html', 'w', encoding='utf-8') as f:
    f.write(mangobloom_content)

# ─── STEP 2: Fix nav dropdown + footer in all hotel pages ────────────────────
hotel_pages = list(FOOTER_ADDRESSES.keys())
all_pages = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['slider.html', 'home.html']]

print("\nFixing nav dropdowns and footers in all pages...")
for page in all_pages:
    if not os.path.exists(page):
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix nav dropdown
    content = fix_nav_dropdown(content)

    # Fix footer address for hotel pages
    if page in FOOTER_ADDRESSES:
        info = FOOTER_ADDRESSES[page]
        content = fix_footer_contact(content, info['name'], info['addr'])

    if content != original:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [UPDATED] {page}")
    else:
        print(f"  [SKIP] {page} - no changes detected")

print("\nDone!")
