import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la pestaña y Estilo (CSS) para que sea Morado Oscuro
st.set_page_config(page_title="BitPlay.io | Juegos Gratis", layout="wide", page_icon="🎮")

st.markdown("""
    <style>
    /* Fondo morado oscuro */
    .stApp {
        background-color: #1a0a2e;
        color: #ffffff;
    }
    /* Estilo para las tarjetas de juegos */
    .game-card {
        background-color: #2d1b4d;
        border-radius: 15px;
        padding: 10px;
        text-align: center;
        border: 2px solid #7000ff;
        transition: 0.3s;
    }
    .game-card:hover {
        border-color: #00f2ff;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Encabezado con tu Logo
# Nota: Asegúrate de subir tu logo al repo con el nombre 'logo.png'
col_logo, col_vacia = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png", width=150)
    except:
        st.title("👾 BitPlay.io")

# 3. Buscador y Categorías
st.sidebar.title("🎮 Menú Principal")
categoria = st.sidebar.radio("Categorías:", ["Todos", "Acción", "Aventura", "Puzzles"])

st.write("---")
st.subheader("🔥 Juegos Destacados")

# 4. Cuadrícula de Juegos (PC-Phone Friendly)
# Usamos columnas que Streamlit adapta automáticamente
cols = st.columns([1, 1, 1])

# Simularemos 3 juegos para empezar (puedes añadir miles después)
# Los links de 'url' son de ejemplo, aquí pegarás los de GamePix/Famobi
juegos = [
    {"titulo": "Hextris", "url": "https://hextris.io/"},
    {"titulo": "2048", "url": "https://play2048.co/"},
    {"titulo": "Tower Game", "url": "https://tower-game.github.io/"}
]

for i, juego in enumerate(juegos):
    with cols[i % 3]:
        st.markdown(f'<div class="game-card"><h3>{juego["titulo"]}</h3></div>', unsafe_allow_html=True)
        # El componente iframe es el que carga el juego real
        components.iframe(juego["url"], height=450, scrolling=True)
        st.button(f"Votar 👍", key=f"btn_{i}")

st.sidebar.info("BitPlay.io - Versión Alpha (Gasto $0)")
