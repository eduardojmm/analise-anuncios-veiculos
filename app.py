# Importando as bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

# Adicionando cabeçalho
st.header('Análise de dados de anúncios de vendas de carros')

# Carregando os dados
car_data = pd.read_csv('vehicles.csv')

# Criando as caixas de seleção
build_hist = st.checkbox('Criar histograma')
build_scatter = st.checkbox('Criar gráfico de dispersão')

# Criando o histograma
if build_hist:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Criando o gráfico de dispersão
if build_scatter:
    st.write('Criando um gráfico de dispersão para odometer vs preço')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
