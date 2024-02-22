# PL2024

## Autor 

**Nome:** Ana Joao Alves

**ID:** A95128

# Explicação do Código

Este é um breve resumo do que o código Python fornecido faz. O código é projetado para converter texto escrito em Markdown para HTML. Vamos analisar cada parte do código:

## Função `markdown_to_html(markdown_text)`

Esta função recebe uma string contendo texto em formato Markdown como entrada e utiliza expressões regulares para encontrar padrões específicos no texto Markdown. Em seguida, substitui esses padrões pelos equivalentes em HTML. 
- Títulos Markdown são convertidos para tags HTML de cabeçalho (`<h1>`, `<h2>`, etc.).
- Negrito e itálico são convertidos para tags HTML `<b>` e `<i>`, respectivamente.
- Listas ordenadas e não ordenadas são convertidas para tags HTML `<ol>` e `<ul>`, com cada item da lista convertido para uma tag `<li>`.
- Imagens e links Markdown são convertidos para as tags HTML `<img>` e `<a>`, respectivamente.
- Linha horizontal (`---`) é convertida para a tag HTML `<hr>`.
- Citação em bloco (`> texto`) é convertida para a tag HTML `<blockquote>`.
- Blocos de código (delimitados por ``` ... ```) são convertidos para a tag HTML `<code>`.

## Função `main()`

Esta função é a função principal do programa. Ela lê o texto Markdown da entrada padrão, chama a função `markdown_to_html()` para converter o texto Markdown em HTML e escreve o HTML resultante em um arquivo chamado `'output.html'`.

