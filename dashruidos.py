import streamlit as st
import pandas as pd

#print("Hello World!")
st.title("Projeto Ruído Zero 🎈")
codigo = st.text_input("Digite um laboratório")
if st.button("Mostrar Ruídos"):
    st.balloons()
    st.success(f"Laboratório: {codigo or 'Não Selecionado'}")

# dados dos ruidos

df_ruidos = pd.read_csv('ruidos.csv',sep=";")
st.dataframe(df_ruidos)