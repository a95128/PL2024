# PL2024

## Autor 

**Nome:** Ana Joao Alves

**ID:** A95128

# ENUNCIADO


Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

Select id, nome, salario From empregados Where salario >= 820


## IMPLEMENTAÇÃO

O código implementa uma função tokenize() que divide uma sequência de texto em tokens para uma linguagem SQL simplificada.
Ele define padrões de expressão regular para identificar palavras-chave (select, from, where), identificadores (ID), operadores de comparação (SIGNAL), números (NUMBER) e outros símbolos.
Ao iterar sobre o texto, o código reconhece e classifica os tokens, considerando também operadores de comparação como tokens distintos de operadores.
A saída é uma lista de tuplos contendo o tipo de token, seu valor, a linha e a posição na linha em que foram encontrados.
Isso permite analisar consultas SQL básicas e identificar os seus componentes individuais para posterior processamento.
