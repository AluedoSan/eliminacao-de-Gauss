linha = int(input('Linhas: '))
coluna = int(input('Coluna: '))
matriz = []
for i in range(linha):
    linhas = []
    for j in range(coluna):
        valor = int(input(f'Valor do {i}x{j}: '))
        linhas.append(valor)
    matriz.append(linhas)

print('Matriz:')
for linhas in matriz:
    print(linhas)

a1 = matriz
a1[0][0] = matriz[1][0] / matriz[0][0]

print(9*'-')
for linhas in a1:
    print(linhas)