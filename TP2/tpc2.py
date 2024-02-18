import sys
import re

def markdown_to_html(markdown_text):
    # Cabeçalhos
    markdown_text = re.sub(r'^#{1}\s+(.+?)\s*$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^#{2}\s+(.+?)\s*$', r'<h2>\1</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^#{3}\s+(.+?)\s*$', r'<h3>\1</h3>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^#{4}\s+(.+?)\s*$', r'<h4>\1</h4>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^#{5}\s+(.+?)\s*$', r'<h5>\1</h5>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^#{6}\s+(.+?)\s*$', r'<h6>\1</h6>', markdown_text, flags=re.MULTILINE)

    # Citação em bloco
    markdown_text = re.sub(r'^>\s(.*?)$', r'<blockquote>\1</blockquote>', markdown_text, flags=re.MULTILINE)

    # Lista não ordenada
    markdown_text = re.sub(r'^-\s+(.+)', r'<ul>\n<li>\1</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'</li>\n<ul>', r'</li>\n</ul>\n<ul>', markdown_text)
    markdown_text += '</ul>'

    # Lista ordenada
    markdown_text = re.sub(r'(\d+\.\s+.*\n?)+', r'<ol>\g<0></ol>', markdown_text)
    markdown_text = re.sub(r'\d+\.\s+(.*)', r'<li>\1</li>\n', markdown_text)

    # Imagem
    markdown_text = re.sub(r'\!{1}\[{1}(.*?)\]{1}\({1}(.*?)\){1}', r'<img src="\2" alt="\1"/>', markdown_text)

    # Link
    markdown_text = re.sub(r'\[{1}(.*?)\]{1}\({1}(.*?)\){1}', r'<a href="\2">\1</a>', markdown_text)

    # Linha horizontal
    markdown_text = re.sub(r'\-{3}', r'<hr>', markdown_text)

    # Código
    markdown_text = re.sub(r'```(.+?)```', r'<code>\1</code>', markdown_text)

    # Negrito
    markdown_text = re.sub(r'\*{2}(.*?)\*{2}', r'<b>\1</b>', markdown_text)

    # Itálico
    markdown_text = re.sub(r'\*{1}(.*?)\*{1}', r'<i>\1</i>', markdown_text)

    return markdown_text

def main():
    markdown_text = sys.stdin.read()
    html_text = markdown_to_html(markdown_text)
    with open('output.html', 'w') as file:
        file.write(html_text)

if __name__ == "__main__":
    main()