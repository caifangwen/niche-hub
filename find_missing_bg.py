import os, re

all_card_classes = ['profile-card', 'steel-card', 'region-card', 'care-card', 'wood-card',
    'decision-card', 'material-card', 'process-card', 'system-card', 'phase-card',
    'partner-card', 'cost-card', 'knife-type-card', 'evolution-card', 'ritual-card',
    'blade-shape-card', 'lock-card', 'use-case-card', 'metric-card', 'cost-band-card',
    'region-overview-card', 'storage-card', 'steel-care-card', 'workflow-card',
    'type-hero-card', 'care-hero-card', 'nav-card', 'tier-card', 'vs-hero-card']

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    content = open(f, 'r', encoding='utf-8-sig').read()
    
    for cls in all_card_classes:
        pattern = r'<div class="' + re.escape(cls) + '"[^>]*>'
        matches = list(re.finditer(pattern, content))
        if not matches:
            continue
        missing = []
        for m in matches:
            snippet = content[m.start():m.start()+300]
            if 'background-image' not in snippet:
                # Extract title
                title_m = re.search(r'<h[34][^>]*>(.*?)</h[34]>', snippet)
                title = title_m.group(1).strip()[:40] if title_m else 'NO TITLE'
                missing.append(title)
        if missing:
            print(f'{f} {cls}: {len(missing)}/{len(matches)} missing')
            for t in missing[:3]:
                print(f'  - {t}')
