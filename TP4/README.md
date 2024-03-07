# PL2024

## Autor 

**Nome:** Ana Joao Alves

**ID:** A95128

# ENUNCIADO

O código que se segue é de uma implementação de analisador léxico para "SELECT id, nome, salario FROM empregados WHERE salario <= 820 + 10 * 2 - 5"


##IMPLEMENTAÇÃO

Numa primeira fase é definido uma token specification que a da elemento da lista(nome do token) é associado um padrãoda expressão regular que será usada para identificar o token.
O terceiro eleemento é opcional e é uma flag para a compilação da expressão regular.


Para cada correspondência encontrada pela expressão regular, o tipo de token é determinado com base no nome do grupo correspondente. Dependendo do tipo de token, suas informações (tipo, valor, linha, posição) são adicionadas a uma lista de tokens reconhecidos.



**Fotografia:** ![Texto Alternativo](output.png)