import sys

sys.stdin.readline()

linhas = sys.stdin.readlines()

modalidades = []
resultados = []
idades = []
tuplos_idades = []

for linha in linhas:
   campos = linha.split(',') 
   idades.append(campos[5])
   modalidades.append(campos[8].lower())
   resultados.append(campos[12])
   tuplos_idades.append((campos[3] + " " + campos[4], campos[5]))


#modalidades por odem alfabetica
filter_modalidades = sorted(set(modalidades))

#Percentagens de atletas aptos e inaptos para a prática desportiva

numero_atletas = len(resultados)

aptos = resultados.count('true\n')
naptos = resultados.count('false\n')

atletas_aptos = (aptos/numero_atletas)*100
atletas_naptos = (naptos/numero_atletas)*100

#Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...


faixas_etarias = [(20,24),(25,29),(30,34),(35,39)]

grupos = {escalao: [] for escalao in faixas_etarias}

# Atribuir idades às faixas etárias correspondentes
for nome, idade in tuplos_idades:
    for faixa in faixas_etarias:
        if faixa[0] <= int(idade) <= faixa[1]:
            grupos[faixa].append((nome, idade))
            

# Ordenar as faixas etárias
faixas_ordenadas = sorted(grupos.items(), key=lambda x: x[0])

# Imprimir os grupos

print("Modalidades: ", filter_modalidades)
print("Percentagem de atletas aptos: ", atletas_aptos ,"%")
print("Percentagem de atletas inaptos: ", atletas_naptos , "%")

for intervalo, valores in faixas_ordenadas:
    print(f"Intervalo {intervalo}: {valores}")
    print(f"Numero de atletas: {len(valores)} Percentagem: {(len(valores)/numero_atletas)*100} %")