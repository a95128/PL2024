import json
import ply.lex as lex

SALDO = 0.0
insert_coin = False
insert_product = False  # Flag to indicate product selection

with open('produtos.json', 'r') as json_file:
    produtos = json.load(json_file)["stock"]

tokens = (
    'OPERATION',
    'COIN',
    'ID',
    'COMMA',
    'POINT'
)

t_COMMA = r','
t_ignore = ' \t'

def t_ID(t):
    r'[A-Z]\d+'
    global SALDO
    if insert_product: 
        selected_product_id = t.value
        for produto in produtos:
            if selected_product_id == produto['cod'] and SALDO >= produto['preco']:
                print(f"Pode retirar o produto dispensado {produto['nome']}")
                produto['quant'] -= 1
                SALDO -= produto['preco']
                print(f"Saldo = {SALDO}")
                return
        print("Saldo insuficiente para satisfazer o seu pedido")
        print(f"Saldo = {SALDO}; Pedido = {produto['preco']}")

def t_OPERATION(t):
    r'\b[A-Z]+\b'
    global insert_coin, insert_product

    if t.value == 'LISTAR':
        for produto in produtos:
            print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")
    
    if t.value == 'MOEDA':
        insert_coin = True
        insert_product = False  

    if t.value == 'SELECIONAR':
        insert_product = True
        insert_coin = False 

def t_POINT(t):
    r'\.'
    print(f"Saldo = {SALDO}")

def t_COIN(t):
    r'\d+[ec]'
    global SALDO
    
    if insert_coin:
        if t.value.endswith('e'):
            SALDO += float(t.value[:-1])
        else:
            SALDO += float(t.value[:-1]) * 0.01

def t_error(t):
    print("Caractere inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def readinput(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break

while True:
    user_input = input(">> ")
    if user_input == "SAIR":
        break
    readinput(user_input)
