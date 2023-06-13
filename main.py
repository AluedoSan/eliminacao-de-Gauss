import streamlit as st
import pandas as pd
import numpy as np


age_title = st.title("")
age = st.slider('', 0, 10)

side_sist = st.sidebar.radio(
    ("Selecione o sistema: "),
    ('Eliminação de Gauss', 'Gauss - Seidel'))

if side_sist == 'Eliminação de Gauss':
    age_title = st.title("Eliminação de Gauss")
elif side_sist == 'Gauss - Seidel':
    age_title = st.title("Gauss - Seidel")   


colum = st.columns(age + 1)
linhas = []


for i in range(age):
    linha = []
    for j in range(age + 1):
        valor = st.sidebar.number_input(f'Valor do {i+1}x{j+1}: ', step=1)
        linha.append(valor)
    linhas.append(linha)

matrix = np.array(linhas, dtype=float)
executar = st.button("Executar ✅")

if side_sist == 'Eliminação de Gauss':
    if executar:
        df = pd.DataFrame(
            matrix,
            columns=('coluna %d' % i for i in range(age+1)))
        st.dataframe(df)
        for i in range(age):
            for j in range(i+1, age):
                pivo = matrix[j, i] / matrix[i, i]
                matrix[j, i:] -= pivo * matrix[i, i:]
                st.dataframe(matrix)

# Obtendo a solução
        solucao = np.zeros(age)
        solucao[age - 1] = matrix[age - 1, age] / matrix[age - 1, age - 1]

        for i in range(age - 2, -1, -1):
            solucao[i] = (matrix[i, age] - np.dot(matrix[i, i+1:age], solucao[i+1:age])) / matrix[i, i]
        st.dataframe(solucao)

        L = np.eye(age)
        U = matrix[:, :-1]

        # Eliminação de Gauss com pivotação parcial
        for i in range(age):
            # Procura o máximo valor absoluto na coluna atual (a partir da linha i)
            max_idx = np.argmax(np.abs(U[i:, i])) + i

            if U[max_idx, i] == 0:
                raise ValueError("Sistema singular: não é possível prosseguir com a pivotação parcial.")

            # Troca as linhas i e max_idx em U e L
            U[[i, max_idx]] = U[[max_idx, i]]
            L[[i, max_idx], :i] = L[[max_idx, i], :i]

            for j in range(i+1, age):
                pivo = U[j, i] / U[i, i]
                U[j, i:] -= pivo * U[i, i:]
                L[j, i] = pivo
        st.header("Sistema U")
        st.dataframe(U)
        st.header("Sistema L")
        st.dataframe(L)

elif side_sist == 'Gauss - Seidel':
    tolerance = st.number_input("Eplison")
    if executar:
        df = pd.DataFrame(
            matrix,
            columns=('coluna %d' % i for i in range(age+1)))
        st.dataframe(df)

        A = matrix[:, :-1]
        b = matrix[:, -1]

# Inicializa a solução
        x = np.zeros(age)

# Número máximo de iterações e tolerância
        max_iter = 100

# Iterações do método de Gauss-Seidel
        for _ in range(max_iter):
            x_prev = np.copy(x)
            for i in range(age):
                sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_prev[i+1:])
                x[i] = (b[i] - sigma) / A[i, i]
            if np.linalg.norm(x - x_prev) < tolerance:
                break
        st.write(x)
