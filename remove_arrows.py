import glob, re
from bs4 import BeautifulSoup

def process_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    changed = False
    
    # 1. Remove trailing " →" from <a class="btn"> or <a class="btn-text">
    for a in soup.find_all('a'):
        classes = a.get('class', [])
        if 'btn' in classes or 'btn-text' in classes:
            text = a.get_text()
            if text.endswith(' →'):
                new_text = text[:-2]
                # Clear all contents and put back the modified text
                # But preserve child tags if any (unlikely for these simple links)
                a.string = new_text
                changed = True
    
    # 2. Clear .step-arrow spans
    for span in soup.find_all('span', class_='step-arrow'):
        span.string = ''
        changed = True
    
    # 3. Clear breadcrumb arrows: .crumbs.series-crumb span
    for div in soup.find_all('div', class_='crumbs series-crumb'):
        for span in div.find_all('span'):
            if span.string and '→' in span.string:
                span.string = ''
                changed = True
    
    # 4. Remove trailing " →" from .factory-cta direct text
    for div in soup.find_all('div', class_='factory-cta'):
        # Handle cases where factory-cta has direct text node (no <a>)
        if div.string and div.string.endswith(' →'):
            div.string = div.string[:-2]
            changed = True
        # Also handle mixed content: some text nodes mixed with <a> tags
        # We already handled <a> tags above, now clean up stray text nodes
        for child in div.children:
            if isinstance(child, str):
                stripped = child.strip()
                if stripped == '→':
                    child.replace_with('')
                    changed = True
    
    # 5. Remove stray " →" text nodes in .steel-links-row and .nav-card
    for cls in ['steel-links-row', 'nav-card', 'nav-cards', 'nav-c']:
        for elem in soup.find_all(class_=cls):
            for child in elem.children:
                if isinstance(child, str):
                    stripped = child.strip()
                    if stripped == '→':
                        child.replace_with('')
                        changed = True
    
    # 6. Remove stray " →" after disabled spans like <span class="btn-text" style="opacity:0.6;cursor:default;">1075</span> →
    # This catches any text node that is just " →" or "→" hanging around in divs
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        if parent and parent.name in ['p', 'div']:
            # Skip content text inside paragraphs or FAQ answers
            if 'faq-a' in parent.get('class', []) or 'data-label' in parent.get('class', []):
                continue
        stripped = text_node.strip()
        if stripped == '→' or stripped == '→' or stripped == '→':
            # Only remove if it's not inside a link (already handled) and not inside content elements
            if parent and parent.name not in ['a']:
                text_node.replace_with('')
                changed = True
    
    if changed:
        # Write back preserving approximate formatting
        # Use prettify() for clean output, but it may alter whitespace significantly
        # For these HTML files, let's use str(soup) which is closer to original
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f'Updated: {filepath}')
    else:
        print(f'No changes: {filepath}')

for html_file in glob.glob('*.html'):
    process_html(html_file)
