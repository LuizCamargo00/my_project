import pandas as pd
import plotly.express as px
import streamlit as st

# Título da aplicação
st.title("Visualização de Dados de Veículos")

# Leitura dos dados
car_data = pd.read_csv('vehicles.csv')

# Botões para selecionar o gráfico
if st.button('Mostrar Histograma da Quilometragem'):
    st.subheader("Histograma da Quilometragem (odometer)")
    fig = px.histogram(car_data, x="odometer", 
                    title="Distribuição de Quilometragem")
    st.plotly_chart(fig)

if st.button('Mostrar Dispersão: Quilometragem vs Preço'):
    st.subheader("Gráfico de Dispersão: Quilometragem vs Preço")
    fig = px.scatter(car_data, x="odometer", y="price",
                    title="Relação entre Quilometragem e Preço")
    st.plotly_chart(fig)
