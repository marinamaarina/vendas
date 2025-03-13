import streamlit as st
import pandas as pd
import folium
import matplotlib.pyplot as plt
from streamlit_folium import folium_static

# Dados das zonas, bairros e vias principais
data = {
    'Zona': ['Zona Central', 'Zona Norte', 'Zona Sul', 'Zona Leste', 'Zona Oeste', 'Zona Periférica'],
    'Bairros': [
        ['Centro', 'Brasil', 'Morada da Colina', 'Fundinho', 'Lídice', 'Osvaldo Resende', 'Segismundo Pereira'],
        ['Tibery', 'Jardim Canadá', 'Santa Rosa', 'Jardim Ipanema', 'São Jorge', 'Industrial'],
        ['Santa Mônica', 'Jardim Patrícia', 'Parque do Sabiá', 'Alvorada', 'Universitário', 'Marta Helena'],
        ['Chácaras Tubalina', 'Martins', 'São Sebastião', 'Chácara do Sol', 'Rosalvo', 'Luizote de Freitas'],
        ['Jardim Europa', 'Jardim Brasília', 'Novo Mundo', 'Jardim das Palmeiras', 'Leste Industrial'],
        ['Cidade Jardim', 'São Vicente', 'Luizote de Freitas', 'Dom Almir', 'Jardim Sorrilândia', 'Boa Vista']
    ],
    'Principais Vias': [
        ['Av. João Naves', 'Av. Rondon Pacheco', 'Rua Getúlio Vargas'],
        ['Av. João Naves', 'Av. Três Moinhos', 'Rua da Balsa'],
        ['Av. João Naves', 'Av. Jundiaí', 'Av. Rio Branco'],
        ['Av. Getúlio Vargas', 'Av. Ester Furquim', 'Av. Cesário Alvim'],
        ['Av. Cesário Alvim', 'Av. Paulo Gracindo', 'Av. JK'],
        ['Av. Luizote', 'Av. Mário Palmério', 'Av. Anselmo Alves']
    ]
}

df = pd.DataFrame(data)

# Pontos de Estoque
pontos_estoque = {
    "📍 Santa Mônica (Estoque)": (-18.9395, -48.2820),
    "📍 Madalena (Estoque)": (-18.9100, -48.3000)
}

# --- Setores com Maior Consumo de Lixo ---
setores_consumo = {
    "Comércio (Supermercados, Restaurantes)": ["Centro", "Brasil", "Segismundo Pereira", "Morada da Colina"],
    "Indústria": ["Tibery", "Jardim Ipanema", "Leste Industrial", "São Jorge"],
    "Saúde (Hospitais, Clínicas)": ["Santa Mônica", "Jardim Patrícia"],
    "Construção Civil": ["Chácaras Tubalina", "Martins", "São Sebastião"]
}

# --- Layout ---
st.set_page_config(page_title="Gestão de Vendas", layout="wide")
st.markdown("<h1 style='text-align: center; color: #D72638;'>🚪 Estratégia de Vendas Porta a Porta</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid #D72638'>", unsafe_allow_html=True)

# --- Selecione a Zona ---
zona_selecionada = st.selectbox('🔍 Escolha uma Zona para Vender:', df['Zona'])

# --- Exibição de Dados e Setores de Consumo ---
if zona_selecionada:
    zona_info = df[df['Zona'] == zona_selecionada].iloc[0]
    st.subheader(f"📌 Bairros na {zona_selecionada}")
    
    # Exibir setores com maior consumo
    st.write("🔑 Setores de Consumo de Lixo na Zona:")
    for setor, bairros in setores_consumo.items():
        st.write(f"**{setor}**: {', '.join(bairros)}")

    # Indicador de vendas por setor (exemplo simples)
    vendas_setores = {"Comércio": 30, "Indústria": 20, "Saúde": 10, "Construção": 15}
    st.subheader("📊 Gráfico de Vendas por Setor")
    st.bar_chart(vendas_setores)

# --- Mapa Interativo ---
st.subheader("🗺️ Mapa de Vendas")
mapa = folium.Map(location=[-18.9186, -48.2769], zoom_start=12)

# Marcar pontos de estoque
for nome, coord in pontos_estoque.items():
    folium.Marker(
        location=coord,
        popup=nome,
        tooltip=nome,
        icon=folium.Icon(color="green")
    ).add_to(mapa)

folium_static(mapa)
