# HOW TO ADD PHOTOS TO THE GALLERY
**File:** `gallery.html`  
**Image Folder:** `assets/img/`

---

## STEP 1 — Prepare Your Image

- Format: `.jpg`, `.png`, or `.webp`
- Minimum size: 1200 × 800 px
- File size: keep under 300 KB
- Naming: lowercase, no spaces (e.g. `la-perle-pool.jpg`)

---

## STEP 2 — Copy the Image File

Put your image inside this folder:

```
assets/img/
```

---

## STEP 3 — Open gallery.html

Find the section for the property you want to add the photo to.
Each section has a comment like:

```
<!-- ===== LA PERLE RIVER RESORT ===== -->
```

---

## STEP 4 — Copy This Code and Paste It

Copy the block below, paste it inside the `<div class="gl-tile-grid">` of the correct property:

```html
<div class="gl-tile" data-prop="PROPERTY" data-cat="CATEGORY" data-title="Image Title" data-caption="Property Name – Image Title">
    <img src="assets/img/YOUR-IMAGE.jpg" alt="Describe the image" loading="lazy">
    <div class="gl-tile-overlay">
        <div class="gl-tile-label">
            <h6>Image Title</h6>
            <span>Category Name</span>
        </div>
    </div>
</div>
```

> Use `class="gl-tile featured"` instead of just `class="gl-tile"` for a wide panoramic image (spans 2 columns).

---

## STEP 5 — Replace the Values

### data-prop (which property)

| Property                              | Use this value      |
|---------------------------------------|---------------------|
| La Perle River Resort, Jim Corbett    | `la-perle`          |
| The Banyan Retreat, Jim Corbett       | `banyan`            |
| Excel Hotels & Resorts, Jim Corbett   | `excel-corbett`     |
| Excel Hotels & Resorts, Nainital      | `excel-nainital`    |
| Excel Hotels & Resorts, Bhimtal       | `excel-bhimtal`     |
| Mangobloom River Resort, Jim Corbett  | `mangobloom`        |

### data-cat (which category)

| Category         | Use this value  | Used for                              |
|------------------|-----------------|---------------------------------------|
| Property/Exterior| `property`      | Aerial, exterior, resort grounds      |
| Rooms & Suites   | `rooms`         | Bedrooms, suites, bathrooms           |
| Dining           | `dining`        | Restaurant, bar, food photos          |
| Experiences      | `experiences`   | Pool, safari, spa, activities, bonfire|
| Events           | `events`        | Weddings, conferences, parties        |

---

## STEP 6 — Full Example

Adding a pool photo to La Perle:

```html
<div class="gl-tile" data-prop="la-perle" data-cat="experiences" data-title="Infinity Pool" data-caption="La Perle River Resort – Infinity Pool">
    <img src="assets/img/la-perle-pool.jpg" alt="Infinity pool at La Perle" loading="lazy">
    <div class="gl-tile-overlay">
        <div class="gl-tile-label">
            <h6>Infinity Pool</h6>
            <span>Experiences</span>
        </div>
    </div>
</div>
```

---

## STEP 7 — Save and Test

1. Save `gallery.html`
2. Open browser: `http://localhost:5000/gallery.html`
3. Press **Ctrl + Shift + R** (hard refresh)
4. Check: click the property filter → your image should appear
5. Check: click the category filter → image should appear
6. Check: click the image → lightbox should open with caption

---

## PROPERTY SECTION LOCATIONS IN gallery.html

| Property              | Search for this text in the file                  |
|-----------------------|---------------------------------------------------|
| La Perle              | `<!-- ===== LA PERLE RIVER RESORT =====`          |
| Banyan Retreat        | `<!-- ===== THE BANYAN RETREAT =====`             |
| Excel Jim Corbett     | `<!-- ===== EXCEL HOTELS – JIM CORBETT =====`     |
| Excel Nainital        | `<!-- ===== EXCEL HOTELS – NAINITAL =====`        |
| Excel Bhimtal         | `<!-- ===== EXCEL HOTELS – BHIMTAL =====`         |
| Mangobloom            | `<!-- ===== MANGOBLOOM RIVER RESORT =====`        |

---

## CHECKLIST BEFORE SAVING

- [ ] Image file is in `assets/img/`
- [ ] File name is lowercase with no spaces
- [ ] `data-prop` is set to the correct property value
- [ ] `data-cat` is set to the correct category value
- [ ] `data-title` is filled in
- [ ] `data-caption` is filled in (include the property name)
- [ ] `alt` text is written
- [ ] `loading="lazy"` is present
- [ ] Tile is pasted inside `<div class="gl-tile-grid">` of the correct section
- [ ] Tested in browser with hard refresh
