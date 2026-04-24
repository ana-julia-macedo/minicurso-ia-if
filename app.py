import streamlit as st
import time

# Função para aplicar fundo
def set_fundo(cor1, cor2):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, {cor1}, {cor2});
        }}
        </style>
    """, unsafe_allow_html=True)

# Estado inicial (rosa)
if "bg" not in st.session_state:
    st.session_state.bg = ("#ffc0cb", "#ffe4e1")

# Aplica fundo atual
set_fundo(*st.session_state.bg)

# Estilo geral
st.markdown("""
    <style>
    h1 {
        color: black;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Estrutura original
st.title("Calculadora de Notas do IF")

n1 = st.text_input("Introduza a Nota 1")
n2 = st.text_input("Introduza a Nota 2")

if st.button("Calcular Média"):
    with st.spinner("Calculando..."):
        time.sleep(1)

    try:
        nota1 = float(n1.strip().replace(",", "."))
        nota2 = float(n2.strip().replace(",", "."))

        media = (nota1 + nota2) / 2

        st.write("A tua média é:", round(media, 2))

        # Condições
        if media > 6.5:
            st.success("🎉 Excelente resultado!")
            st.balloons()
            st.session_state.bg = ("#ffc0cb", "#ffe4e1")  # mantém rosa

        else:
            st.error("❌ Média abaixo de 6.5")
            st.session_state.bg = ("#ff4d4d", "#8b0000")  # vermelho

        # Reaplica o fundo após clique
        set_fundo(*st.session_state.bg)

    except ValueError:
        st.error("Digite números válidos (ex: 7,5 ou 7.5).")
