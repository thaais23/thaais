
import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Portafolio de Thais", layout="wide")

# Barra lateral
st.sidebar.title("📌 Navegación")
seccion = st.sidebar.radio("Ir a:", [
    "🏠 Home",
    "📄 Resume",
    "💼 Projects",
    "📚 Research",
    "🏅 Achievements",
    "🎨 Hobbies",
    "📞 Contact"
])

# HOME
if seccion == "🏠 Home":
    st.title("Hola, soy Thais Choque")
    st.subheader("Estudiante de Comunicación Audiovisual en la PUCP")
    st.write("""
    Me interesa aprender sobre herramientas visuales, creación de contenido y formas de narrar historias a través de imágenes. Este portafolio es un reflejo de lo que estoy explorando en mi carrera y mi proceso como comunicadora visual en formación.
    """)
    st.header("¿Quieres saber algo sobre mí?")
    pregunta = st.text_input("Escribe tu pregunta aquí")
    if pregunta:
        st.write("Gracias por tu interés. ¡Sigo en proceso de aprender cada día!")

# RESUME
elif seccion == "📄 Resume":
    st.header("Resumen Académico")
    st.write("""
    🎓 **Educación**  
    - PUCP – Comunicación Audiovisual (5to ciclo)

    🛠️ **Habilidades**  
    - Edición de video (básico)  
    - Fotografía y composición visual  
    - Trabajo en equipo y responsabilidad  
    - Interés en herramientas digitales (como Streamlit)

    🌐 **Idiomas**  
    - Español (nativo)  
    - Inglés (intermedio)
    """)

# PROJECTS
elif seccion == "💼 Projects":
    st.header("Proyectos Académicos")

    st.subheader("📷 Proyecto fotográfico universitario")
    st.write("Serie de fotografías realizadas para un curso de Comunicación Audiovisual. Se trabajó luz natural, retrato, composición y color.")

    st.subheader("🎞️ Trabajo de análisis visual")
    st.write("Análisis de escenas cinematográficas como parte de cursos de lenguaje audiovisual. Enfoque en planos, ritmo y narrativa visual.")

    st.subheader("📚 Proyecto de narrativa audiovisual")
    st.write("Trabajo grupal para desarrollar una historia con enfoque visual. Se exploraron ideas, guión y propuesta estética.")

# RESEARCH
elif seccion == "📚 Research":
    st.header("Intereses Académicos")
    st.write("""
    Aún no cuento con investigaciones formales ni publicaciones, pero me interesa aprender más sobre procesos creativos, estética visual y lenguaje audiovisual.
    """)

# ACHIEVEMENTS
elif seccion == "🏅 Achievements":
    st.header("Logros y Participaciones")
    st.write("""
    📌 Participación en trabajos grupales universitarios de producción y análisis audiovisual.  
    🎓 Cursos aprobados en narrativa, lenguaje visual y fotografía.  
    🚀 Sigo en proceso de crecer y construir nuevas experiencias.
    """)

# HOBBIES
elif seccion == "🎨 Hobbies":
    st.header("Mis Pasatiempos")
    st.write("""
    🎧 Escuchar música (K-pop, pop)  
    📺 Ver series coreanas y contenido visual
    """)

# CONTACT
elif seccion == "📞 Contact":
    st.header("Contáctame")
    st.write("""
    📧 Email: thaischoque@email.com  
    💬 ¡Estoy abierta a nuevas ideas y aprendizajes!
    """)
