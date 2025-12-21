import re

filepath = r'c:\Users\Mamabru\Desktop\BADIANI 1932\Badiani Web\badiani-FINAL-V24-CORRECTED.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update .gallery to use calligraphic background with pink color
old_gallery = ".gallery{ background:var(--badiani-pink); padding:90px 20px; text-align:center; position:relative; overflow:hidden; }"
new_gallery = ".gallery{ background: #ff5a9e url('assets/barattolo-tab.png') center/cover no-repeat; padding:90px 20px; text-align:center; position:relative; overflow:hidden; }"

content = content.replace(old_gallery, new_gallery)

# Update .gallery::before to use pink overlay instead of base64 image
# The current ::before has a base64 background image with B pattern, replace with solid pink overlay
pattern = r'\.gallery::before\{[^}]*background-image:url\([^)]+\)[^}]*\}'
replacement = ".gallery::before{ content:''; position:absolute; inset:0; background:rgba(255,90,158,0.5); z-index:0; }"

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Gallery background updated with pink calligraphic image!')
