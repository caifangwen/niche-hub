import re, glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i, line in enumerate(lines, 1):
        if '→' in line:
            has_btn = 'class="btn"' in line or 'class="btn-text"' in line or "class='btn'" in line or "class='btn-text'" in line
            if not has_btn:
                print(f'{f}:{i}: {line.strip()}')
