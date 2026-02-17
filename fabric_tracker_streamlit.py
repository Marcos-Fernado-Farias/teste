import streamlit as st
import json
import os

DATA_FILE = 'fabric_tracker.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'jeans': 0, 'pt': 0}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Carregar dados
data = load_data()

st.title("Rastreador de Resíduos de Tecido")
st.write("Adicione bolsas de Jeans ou PT e veja os totais.")

# Entrada de dados
fabric_type = st.selectbox("Tipo de Tecido", ["Jeans", "PT"])
bags = st.number_input("Quantas Bolsas Foram Colocadas?", min_value=0, step=1)
if st.button("Adicionar Bolsas"):
    data[fabric_type.lower()] += bags
    save_data(data)
    st.success(f"Adicionado {bags} bolsas de {fabric_type}.")

# Exibir totais
st.subheader("Totais Atuais")
st.write(f"Bolsas de Jeans: {data['jeans']}")
st.write(f"Bolsas de PT: {data['pt']}")
st.write(f"Total Geral: {data['jeans'] + data['pt']}")

# Finalizar para coleta (reiniciar)
if st.button("Finalizar para Coleta (Reiniciar Totais)"):
    st.write("Totais Finais:")
    st.write(f"Jeans: {data['jeans']}, PT: {data['pt']}, Total: {data['jeans'] + data['pt']}")
    data = {'jeans': 0, 'pt': 0}
    save_data(data)
    st.success("Totais reiniciados para o próximo ciclo.")