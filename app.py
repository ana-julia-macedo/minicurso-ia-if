import streamlit as st

def set_fundo(cor1, cor2):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, {cor1}, {cor2});
        }}
        </style>
    """, unsafe_allow_html=True)

if "bg" not in st.session_state:
    st.session_state.bg = ("#ffc0cb", "#ffe4e1")

set_fundo(*st.session_state.bg)

st.title("Calculadora de Notas do IF")

n1 = st.number_input("Nota 1", 0.0, 10.0, step=0.1)
n2 = st.number_input("Nota 2", 0.0, 10.0, step=0.1)

if st.button("Calcular Média"):
    media = (n1 + n2) / 2

    st.metric("Média Final", round(media, 2))

    if media >= 6.5:
        st.success("🎉 Excelente resultado!")
        st.balloons()
        st.session_state.bg = ("#ffc0cb", "#ffe4e1")
    else:
        st.error("❌ Média abaixo de 6.5")
        st.session_state.bg = ("#ff4d4d", "#8b0000")

    set_fundo(*st.session_state.bg)
