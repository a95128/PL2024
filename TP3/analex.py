import ply.lex as lex
import re
import sys

states = (
    ('onativo', 'exclusive'),
)


tokens = (
    'ON',
    'OFF',
    'EQUAL',
    'NUMBER',
    'STRING', 
)


t_ANY_ignore = r' \t\n'

soma = 0

def t_ON(t):
    r'[Oo][Nn]'
    t.lexer.begin('onativo')
    return t

def t_OFF(t):
    r'[oO][Ff][Ff]'
    return t

def t_NUMBER(t):
    r'\d+'
    return t

def t_STRING(t):
    r'[A-Za-z]'
    return t

def t_onativo_OFF(t):
    r'[oO][Ff][Ff]'
    t.lexer.begin('INITIAL')
    return t

def t_onativo_STRING(t):
    r'[a-zA-Z]'
    return t

def t_onativo_NUMBER(t):
    r'\d+'
    t.lexer.stack.append(t.value)
    return t

def t_ANY_EQUAL(t):
    r'='
    global soma
    while (t.lexer.stack):
        soma += int(t.lexer.stack.pop(-1))
    print(soma)



def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

data = '''
1iMRE7r=HtzkAon8o2sdXVtM0oLoff=zNxZi4t5eqOpZNEqCJaLonK1mMTy3d22=W
offaJ8=uH6sgDxy2xMJoNRQZ7=aAmkmhF4N91eTqqzequb4eYpA34DIojequZtnvw
6LyrPxme0eqZbYZPon82fFbYKoffQXTonOnjjAAzS4=eq1tKe0VQuS89yuoffL
oNCs8rV24P3Eeq1GeAtonjvTK0A5KmKAEaOon1=deqQcZrZ5MBu58HzkequWQ5
XC9Fon83ctoffFHaEQFtN9aIonfjAq9eqW0L6F9W4=eq=2pOQRUgAM56DKoffZ
6BYeq7sYononKZV=eq0K9KdW=VononAid6Uon6GeoffW=onD=OffonEQ=offG=3
9MoNyOn=EQOff7offOn5DSOffOn9OnW=43Uk=OffOnON
'''

lexer = lex.lex()

lexer.stack = list()

lexer.input(data)

for token in lexer:
    print(token)