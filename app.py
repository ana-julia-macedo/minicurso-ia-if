import streamlit as st

st.title("Calculadora de Notas do IF")

n1 = st.text_input("Introduza a Nota 1")
n2 = st.text_input("Introduza a Nota 2")

if st.button("Calcular Média"):
    try:
        # Aceita vírgula ou ponto como decimal
        nota1 = float(n1.replace(",", "."))
        nota2 = float(n2.replace(",", "."))

        media = (nota1 + nota2) / 2

        st.write("A tua média é:", round(media, 2))
    
    except ValueError:
        st.error("Por favor, introduza números válidos (ex: 7.5 ou 7,5).")
