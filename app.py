import streamlit as st

# CSS personalizado
st.markdown("""
    <style>
    /* Fundo geral com tom rosa suave */
    .stApp {
        background: linear-gradient(135deg, #ffc0cb, #ffe4e1);
    }

    /* Título em preto */
    h1 {
        color: black;
        text-align: center;
        font-weight: bold;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        background-color: #fff0f5;
        border: 2px solid #ff69b4;
        border-radius: 10px;
        padding: 8px;
    }

    /* Botão */
    .stButton > button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #ff1493;
    }

    /* Texto */
    .stMarkdown, .stText {
        color: #4a4a4a;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Seu código original (mantido)
st.title("Calculadora de Notas do IF")

n1 = st.text_input("Introduza a Nota 1")
n2 = st.text_input("Introduza a Nota 2")

if st.button("Calcular Média"):
    try:
        nota1 = float(n1.strip().replace(",", "."))
        nota2 = float(n2.strip().replace(",", "."))

        media = (nota1 + nota2) / 2

        st.write("A tua média é:", round(media, 2))

    except ValueError:
        st.error("Digite apenas números válidos (ex: 7,5 ou 7.5).")
