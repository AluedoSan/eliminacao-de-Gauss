import numpy as np

matrix = int(input("Tamanho da matriz: "))

linhas = []

for i in range(matrix):
    linha = []
    for j in range(matrix + 1):
        valor = float(input(f'Valor do {i+1}x{j+1}: '))
        linha.append(valor)
    linhas.append(linha)

matriz = np.array(linhas, dtype=float)

# Eliminação de Gauss
for i in range(matrix):
    if matriz[i, i] == 0:
        for k in range(i + 1, matrix):
            if matriz[k, i] != 0:
                matriz[[i, k]] = matriz[[k, i]]
                break
        else:
            raise ValueError("A matriz não possui solução única.")

    for j in range(i+1, matrix):
        ratio = matriz[j, i] / matriz[i, i]
        matriz[j, i:] -= ratio * matriz[i, i:]

# Obtendo a solução
solucao = np.zeros(matrix)
solucao[matrix - 1] = matriz[matrix - 1, matrix] / matriz[matrix - 1, matrix - 1]

for i in range(matrix - 2, -1, -1):
    solucao[i] = (matriz[i, matrix] - np.dot(matriz[i, i+1:matrix], solucao[i+1:matrix])) / matriz[i, i]

print("Solução:")
print(solucao)
