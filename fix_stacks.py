"""
Fix gallery.html: remove all gl-tile-stack wrapper divs.
The CSS now uses grid-auto-rows + grid-row:span 2 on featured tiles,
so the two "stacked" tiles beside a featured tile just sit naturally
in the grid as regular tiles — no wrapper div needed.
"""
import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Remove opening <div class="gl-tile-stack"> tags
content = re.sub(r'\s*<div class="gl-tile-stack">\s*', '\n                    ', content)

# Step 2: Remove closing </div> that was the stack closing tag
# The stack had exactly 2 .gl-tile children then a </div>.
# After removing the opening tag, there's now an extra </div> per stack.
# We identify them as </div> that appears after the second .gl-tile in what was a stack.
# Simpler: the stack closing </div> appears right after a </div> of a gl-tile (not inside another container).
# Strategy: remove lines that are just whitespace + </div> that don't belong to anything else.

# The stack structure was:
#   <div class="gl-tile-stack">
#     <div class="gl-tile">...</div>
#     <div class="gl-tile">...</div>
#   </div>   <-- this is the extra one to remove

# After our first replace, the stack opening is gone.
# Now each former stack's closing </div> is an orphan.
# We can find them: look for a pattern of gl-tile closing div followed by whitespace+</div>+whitespace+next gl-tile or section end

# Count stacks before
stack_count_before = content.count('gl-tile-stack')
print(f'Remaining gl-tile-stack occurrences: {stack_count_before}')

# Remove the orphan </div> lines — they appear as:
# "                    </div>\n                    <div class=\"gl-tile\"" (no other marker)
# More reliable: find "</div>" lines that come after a gl-tile closing </div> and before another gl-tile or section closer

# Actually cleanest approach: remove <div class="gl-tile-stack"> and its matching </div>
# by parsing. Let's do it fresh on the original.

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace entire stack blocks: <div class="gl-tile-stack">...</div>
# using a regex that matches the outer div and removes only the wrapper
def remove_stack_wrapper(html):
    # Pattern: <div class="gl-tile-stack">\n...tiles...\n</div>
    # We want to keep the inner tiles but remove the outer div
    pattern = re.compile(
        r'<div class="gl-tile-stack">\s*(.*?)\s*</div>',
        re.DOTALL
    )
    # Replace wrapper with just its inner content
    result = pattern.sub(lambda m: m.group(1).strip(), html)
    return result

new_content = remove_stack_wrapper(content)
stacks_after = new_content.count('gl-tile-stack')
print(f'gl-tile-stack after removal: {stacks_after}')
print(f'Original size: {len(content)}, New size: {len(new_content)}')

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done!')
