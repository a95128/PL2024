import sys
import re

def somador_on_off(text):
    analisa_onoff = re.compile(r'\s+on.*?\s+off|=', re.IGNORECASE)
    analisa_inteiros = re.compile(r'[+-]?\d+|=')
    
    matches = analisa_onoff.findall(text)
    
    numero_sinal = []
    
    for match in matches:
        numero_sinal.extend(analisa_inteiros.findall(match))
    
    soma = 0
    for item in numero_sinal:
        if item == '=':
            print(soma)
        else:
            soma += int(item)
    return soma

def main():
    input = sys.stdin.read()
    somador_on_off(input)

if __name__ == '__main__':
    main()