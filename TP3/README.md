# PL2024

## Autor 

**Nome:** Ana Joao Alves

**ID:** A95128

# Explicação do Código

Este é um breve resumo do que o código Python fornecido faz. O código é projetado para somar todos os números entre On/Off e mostrar o resultado aaté um caracter "=". Vamos analisar cada parte do código:

### `somador_on_off(texto)`

Esta função recebe uma string `texto` como entrada e realiza as seguintes etapas:

1. Utiliza expressões regulares para encontrar seções de texto delimitadas pelas palavras "on" e "off" ou pelo sinal de igual "=".
2. Dentro de cada seção delimitada, extrai inteiros juntamente com seus sinais (positivo ou negativo) e "=".
3. Calcula a soma de todos os inteiros encontrados dentro de cada seção.
4. A soma de cada seção é impressa quando encontra "=".

## Função `main()`

Ela lê o ficheiro "input.txt" e chama a função `somador_on_off()` para realizar o cálculo da soma no texto de entrada.
