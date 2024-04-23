import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

car_data.dropna(subset=['odometer'], inplace=True)  # apagando valores nulos


hist_button = st.button('Criar um histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data,
                       x="odometer",
                       title="Estatística de Vendas de Carros por Quilometragem")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    # criar um gráfico de dispersão
    fig2 = px.scatter(car_data,
                      x="odometer",
                      y="price",
                      title="Comparando o preço de venda do veículo com a quilometragem")

    st.plotly_chart(fig2, use_container_width=True)  # exibindo
