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
        valor = st.sidebar.number_input(f'Valor do {i+1}x{j+1}: ', min_value=1)
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
        for i in range(matrix):
    if matriz[i, i] == 0:
        raise ValueError("O pivô não pode ser zero.")

    for j in range(i+1, matrix):
        ratio = matriz[j, i] / matriz[i, i]
        matriz[j, i:] -= ratio * matriz[i, i:]

# Obtendo a solução
solucao = np.zeros(matrix)
solucao[matrix - 1] = matriz[matrix - 1, matrix] / matriz[matrix - 1, matrix - 1]

for i in range(matrix - 2, -1, -1):
    solucao[i] = (matriz[i, matrix] - np.dot(matriz[i, i+1:matrix], solucao[i+1:matrix])) / matriz[i, i]

elif side_sist == 'Gauss - Seidel':
    if executar:
        df = pd.DataFrame(
            matrix,
            columns=('coluna %d' % i for i in range(age+1)))
        st.dataframe(df)
