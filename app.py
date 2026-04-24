import streamlit as st

st.set_page_config(page_title="Calculadora de Notas", page_icon="📊")

st.title("📊 Calculadora de Notas do IF")

st.write("Digite suas notas (pode usar casas decimais, ex: 7.5)")

# Inputs numéricos (já aceitam decimal corretamente)
n1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
n2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

if st.button("Calcular Média"):
    media = (n1 + n2) / 2

    st.subheader(f"Média: {media:.2f}")

    if media >= 6:
        st.success("✅ Aprovado")
    else:
        st.error("❌ Reprovado")
