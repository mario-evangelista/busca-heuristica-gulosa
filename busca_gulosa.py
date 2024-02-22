# Carregar o arquivo
# Abrindo o arquivo 'dados.txt' para leitura
carga = open('dados.txt')

# Lendo a primeira linha para obter o número de itens (numero_inteiro) e a capacidade da mochila (CAP)
linha = carga.readline()
divisor = linha.split(',')
numero_inteiro = int(divisor[0])  # Convertendo o número de itens para inteiro
CAPACIDADE = int(divisor[1])  # Convertendo a capacidade para inteiro

# Inicializando uma lista vazia para armazenar os dados dos itens
dados = []

# Lendo as informações de cada item e armazenando na lista dados
for i in range(0, numero_inteiro):
    linha = carga.readline()
    divisor = linha.split(',')
    row = [int(divisor[0]), int(divisor[1]), int(divisor[2])]  # Convertendo as informações do item para inteiros
    dados.append(row)

# Imprimindo a tabela de dados
print('\nTabela de dados')
print('\nId\tPeso\tValor')
for row in dados:
    print('%d\t%d\t\t%d' % (row[0], row[1], row[2]))

# HEURÍSTICA GULOSA PELO LUCRO

print('\n\nHEURÍSTICA GULOSA PELO LUCRO')

# Ordenando os dados por lucro em ordem decrescente
dados_lucro = sorted(dados, key=lambda row: -row[2])

# Imprimindo a tabela de dados ordenada por lucro
print('\nTabela de dados ordenado por lucro')
print('\nId\tPeso\tValor')
for row in dados_lucro:
    print('%d\t%d\t\t%d' % (row[0], row[1], row[2]))

# Inicializando variáveis para armazenar o peso total, lucro total e um vetor binário
# indicando quais itens foram selecionados
peso_total = 0
lucro_total = 0
vetor_binario = [0] * numero_inteiro

# Imprimindo o estado inicial do vetor binário, peso total e lucro total
print('\nPeso:', peso_total, ' | Lucro:', lucro_total, ' | Vetor:', vetor_binario)

# Iterando sobre os itens ordenados por lucro e selecionando aqueles que cabem na mochila
for obj in dados_lucro:
    if (obj[1] + peso_total <= CAPACIDADE):
        vetor_binario[obj[0] - 1] = 1
        peso_total += obj[1]
        lucro_total += obj[2]

# Imprimindo o estado final do vetor binário, peso total e lucro total
print('\nPeso:', peso_total, ' | Lucro:', lucro_total, ' | Vetor:', vetor_binario)

# HEURÍSTICA GULOSA PELA EFICIÊNCIA

print('\n\nHEURÍSTICA GULOSA PELA EFICIÊNCIA')

# Calculando a eficiência de cada item (valor/peso)
for obj in dados:
    obj.append(obj[2] / obj[1])

# Ordenando os dados por eficiência em ordem decrescente
dados_eficiencia = sorted(dados, key=lambda row: -row[3])

# Imprimindo a tabela de dados ordenada por eficiência
print('\nTabela de dados ordenado por eficiência')
print('\nId\tPeso\tValor\tEficiência')
for row in dados_eficiencia:
    print('%d\t%d\t\t%d\t\t%d' % (row[0], row[1], row[2], row[3]))

# Inicializando variáveis para armazenar o peso total, lucro total e um vetor binário
# indicando quais itens foram selecionados
peso_total_2 = 0
lucro_total_2 = 0
vetor_binario_2 = [0] * numero_inteiro

# Imprimindo o estado inicial do vetor binário, peso total e lucro total
print('\nPeso:', peso_total_2, ' | Lucro:', lucro_total_2, ' | Vetor:', vetor_binario_2)

# Iterando sobre os itens ordenados por eficiência e selecionando aqueles que cabem na mochila
for obj in dados_eficiencia:
    if (obj[1] + peso_total_2 <= CAPACIDADE):
        vetor_binario_2[obj[0] - 1] = 1
        peso_total_2 += obj[1]
        lucro_total_2 += obj[2]

# Imprimindo o estado final do vetor binário, peso total e lucro total
print('\nPeso:', peso_total_2, ' | Lucro:', lucro_total_2, ' | Vetor:', vetor_binario_2)
