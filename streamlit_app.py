import streamlit as st
import streamlit.components.v1 as components

# Configuración base
st.set_page_config(page_title="BitPlay.io", layout="wide", page_icon="🎮")

# --- ESTILO CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .stApp { background-color: #120522; color: white; }
    
    /* Cuadros chiquitos de juegos */
    .game-thumb {
        border: 2px solid #7000ff;
        border-radius: 10px;
        padding: 5px;
        text-align: center;
        cursor: pointer;
        transition: 0.3s;
        background: #1a0a2e;
    }
    .game-thumb:hover { border-color: #00f2ff; transform: scale(1.05); }
    
    /* Barra lateral */
    .css-1d391kg { background-color: #1a0a2e; } 
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE JUEGOS (Ejemplo) ---
# Aquí irás agregando tus miles de juegos
if 'juegos' not in st.session_state:
    st.session_state.juegos = [
        {"id": 1, "nombre": "Hextris", "cat": "Puzzles", "url": "https://hextris.io/", "img": "https://via.placeholder.com/150/7000ff/ffffff?text=Hextris"},
        {"id": 2, "nombre": "Moto X3M", "cat": "Conduccion", "url": "https://games.gamepix.com/play/40141", "img": "https://via.placeholder.com/150/7000ff/ffffff?text=MotoX3M"},
        {"id": 3, "nombre": "Space Invaders", "cat": "Accion", "url": "https://p2.friv.com/z/juegos/space-invaders/juego.html", "img": "https://via.placeholder.com/150/7000ff/ffffff?text=Space"},
    ]

# --- LÓGICA DE NAVEGACIÓN ---
if 'vista' not in st.session_state:
    st.session_state.vista = 'inicio'
if 'juego_actual' not in st.session_state:
    st.session_state.juego_actual = None

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    try:
        st.image("logo.png", width=120)
    except:
        st.header("BitPlay")
    
    st.write("### Categorías")
    cat_seleccionada = st.radio("", ["Todos", "Accion", "Aventura", "Puzzles", "Conduccion"], label_visibility="collapsed")
    
    if st.button("🏠 Volver al Inicio"):
        st.session_state.vista = 'inicio'
        st.rerun()

# --- VISTA DE INICIO (CUADRÍCULA) ---
if st.session_state.vista == 'inicio':
    st.title("🎮 BitPlay.io")
    
    # Filtrar juegos por categoría
    juegos_filtrados = [j for j in st.session_state.juegos if cat_seleccionada == "Todos" or j['cat'] == cat_seleccionada]
    
    # Cuadrícula de cuadros chiquitos (5 columnas para que sean pequeños)
    cols = st.columns(5)
    for i, juego in enumerate(juegos_filtrados):
        with cols[i % 5]:
            st.markdown(f'<div class="game-thumb">', unsafe_allow_html=True)
            st.image(juego['img'], use_container_width=True)
            if st.button(f"Jugar {juego['nombre']}", key=f"btn_{juego['id']}"):
                st.session_state.juego_actual = juego
                st.session_state.vista = 'juego'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# --- VISTA DE JUEGO (REPRODUCTOR) ---
elif st.session_state.vista == 'juego':
    j = st.session_state.juego_actual
    st.markdown(f"<h2 style='text-align: center;'> < {j['nombre']} > </h2>", unsafe_allow_html=True)
    
    # Contenedor del juego
    components.iframe(j['url'], height=600, scrolling=True)
    
    # Botón Pantalla Completa (Instrucción al usuario ya que por seguridad de navegador el iframe tiene límites)
    st.info("💡 Consejo: Muchos juegos tienen su propio botón de pantalla completa abajo a la derecha.")
    
    # Sección de Like/Dislike y Comentarios
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("👍 Me gusta", use_container_width=True)
    with col2:
        st.button("👎 No me gusta", use_container_width=True)
    
    st.write("---")
    st.subheader("💬 Comentarios")
    st.text_input("Escribe qué te pareció el juego...", placeholder="¡Este juego es genial!")
    st.button("Publicar comentario")
