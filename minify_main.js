/**
 * Minify main.js preserving code logic, only stripping JSDoc block comments
 * and single-line // comments that are on their own line (not inline code)
 */
const fs = require('fs');
let js = fs.readFileSync('assets/js/main.js', 'utf8');

// Remove only block comments /* ... */ that are standalone (not in strings)
js = js.replace(/\/\*[\s\S]*?\*\//g, '');

// Remove only comment-only lines (lines that start with optional whitespace then //)
// but NOT lines that have code before the comment
js = js.split('\n').map(line => {
    const trimmed = line.trim();
    if (trimmed.startsWith('//')) return ''; // pure comment line → remove
    return line; // keep code lines (even if they have inline // comments)
}).join('\n');

// Collapse multiple blank lines to one
js = js.replace(/\n{3,}/g, '\n\n').trim();

fs.writeFileSync('assets/js/main.min.js', js);
console.log('Done. Size:', js.length);

// Verify the guard is present
if (js.includes('gl-section')) {
    console.log('✓ gl-section guard is in main.min.js');
} else {
    console.log('✗ gl-section guard MISSING from main.min.js');
}
