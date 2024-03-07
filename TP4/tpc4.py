import re
import sys

def tokenize(code):
    token_specification = [
        ('OP', r'\bselect\b|\bfrom\b|\bwhere\b', re.IGNORECASE),
        ('ID', r'[_A-Za-z][_A-Za-z0-9]*'),
        ('SIGNAL', r'<=|>=|=|<|>', 0),  # Adicionei a flag 0 para desativar a ignorância de maiúsculas e minúsculas
        ('NUMBER', r'\d+(\.\d+)?'),
        ('NEWLINE',  r'\n'),
        ('COMMA',   r','),
        ('SKIP', r'\s+'),
        ('UNKNOWN', r'.')
    ]
    regex_patterns = []
    for name, regex, *flags in token_specification:  # Use *flags para lidar com flags adicionais, se houver
        regex_patterns.append('(?P<{}>{})'.format(name, regex))
    tok_regex = '|'.join(regex_patterns)
    print("Generated regex:", tok_regex)  # Saída de depuração
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    for m in mo:
        for name, regex, *flags in token_specification:
            if m.group(name):
                token_type = name
                if token_type == 'NUMBER':
                    t = ("NUMBER", float(m.group(name)), linha, m.span())
                elif token_type == 'SIGNAL':
                    if m.group(name) in {'<=', '<', '=', '>', '>='}:
                        token_type = 'OPERATOR'
                    t = (token_type, m.group(name), linha, m.span())
                else:
                    t = (token_type, m.group(name), linha, m.span())
                reconhecidos.append(t)
    return reconhecidos

# Exemplo de uso
texto = '''SELECT id, nome, salario FROM empregados WHERE salario <= 820 + 10 * 2 - 5'''
for tok in tokenize(texto):
    print(tok)
