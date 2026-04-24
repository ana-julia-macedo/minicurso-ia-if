import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Notas IF",
    page_icon="📊",
    layout="centered"
)

# Título
st.title("📊 Calculadora de Notas do IF")
st.write("Insira suas notas abaixo para calcular a média automaticamente.")

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    n1 = st.number_input(
        "Nota 1",
        min_value=0.0,
        max_value=10.0,
        step=0.1,
        format="%.2f"
    )

with col2:
    n2 = st.number_input(
        "Nota 2",
        min_value=0.0,
        max_value=10.0,
        step=0.1,
        format="%.2f"
    )

# Botão
if st.button("📊 Calcular Média"):
    media = (n1 + n2) / 2

    st.divider()
    st.subheader(f"🎯 Média Final: {media:.2f}")

    # Classificação
    if media >= 6:
        st.success("✅ Aprovado!")
    elif media >= 4:
        st.warning("⚠️ Recuperação")
    else:
        st.error("❌ Reprovado")

# Rodapé simples
st.divider()
st.caption("Projeto simples com Streamlit • Calculadora de Médias")
