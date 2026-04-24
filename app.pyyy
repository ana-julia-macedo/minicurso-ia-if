import streamlit as st

st.title("📊 Calculadora de Notas do IF")

# Inputs como texto (aceitando decimal)
n1 = st.text_input("Introduza a Nota 1 (ex: 7.5)")
n2 = st.text_input("Introduza a Nota 2 (ex: 8.3)")

if st.button("Calcular Média"):
    try:
        # Substitui vírgula por ponto (importante para quem digita 7,5)
        n1 = float(n1.replace(",", "."))
        n2 = float(n2.replace(",", "."))

        media = (n1 + n2) / 2

        st.success(f"Média: {media:.2f}")

    except ValueError:
        st.error("Por favor, introduza números válidos (ex: 7.5 ou 7,5).")
