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
linhas = age
colunas = age
matriz = []
for i in range(linhas):
    linhas = []
    for j in range(colunas):
        valor = st.number_input(f'Valor do {i+1}x{j+1}: ', min_value=1)
        linhas.append(valor)
    matriz.append(linhas)
executar = st.button("Executar ✅")

if executar:
    df = pd.DataFrame(
        np.random.randn(valor, colunas),
        columns=('coluna %d' % i for i in range(age)))

st.dataframe(df)
