import streamlit as st

def set_estilo():
    st.markdown("""
        <style>

        /* Fundo geral */
        .stApp {
            background: linear-gradient(135deg, #ffe4e1, #ffc0cb);
            font-family: 'Comic Sans MS', cursive;
            animation: fadeIn 1.5s ease-in;
        }

        /* Fade ao carregar */
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        /* Título */
        h1 {
            text-align: center;
            color: #ff69b4;
            font-size: 40px;
            animation: pulse 2s infinite;
        }

        /* Pulsar suave */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Inputs */
        .stNumberInput input {
            border-radius: 15px;
            border: 2px solid #ffb6c1;
            padding: 10px;
        }

        /* Botão animado */
        div.stButton > button {
            background-color: #ffb6c1;
            color: white;
            border-radius: 20px;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            background-color: #ff69b4;
            transform: scale(1.1) rotate(-1deg);
            box-shadow: 0px 0px 15px #ff69b4;
        }

        /* Caixa */
        .box {
            background-color: rgba(255,255,255,0.7);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0px 0px 15px rgba(255,182,193,0.6);
        }

        /* 🌸 Corações flutuando */
        .heart {
            position: fixed;
            bottom: -10px;
            font-size: 20px;
            animation: floatUp 6s linear infinite;
        }

        @keyframes floatUp {
            0% {
                transform: translateY(0) scale(1);
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) scale(1.5);
                opacity: 0;
            }
        }

        </style>
    """, unsafe_allow_html=True)

# 💖 Aplica estilo
set_estilo()

# 💕 Gera corações aleatórios
for i in range(10):
    st.markdown(f"""
        <div class="heart" style="left:{i*10}%;">
            💗
        </div>
    """, unsafe_allow_html=True)

# 🎀 Título
st.markdown("<h1>🎀 Calculadora Fofinha 🎀</h1>", unsafe_allow_html=True)

# 🌸 Caixa
st.markdown('<div class="box">', unsafe_allow_html=True)

n1 = st.number_input("🌸 Nota 1", 0.0, 10.0, step=0.1)
n2 = st.number_input("🌸 Nota 2", 0.0, 10.0, step=0.1)

if st.button("💖 Calcular Média"):
    media = (n1 + n2) / 2

    st.markdown(f"### 💕 Sua média: **{media:.2f}**")

    if media >= 6.5:
        st.success("🌷 Arrasou!! Você foi aprovada 💖✨")
        st.balloons()
    else:
        st.error("🥺 Não foi dessa vez... mas você consegue! 🌱💗")

st.markdown('</div>', unsafe_allow_html=True)
