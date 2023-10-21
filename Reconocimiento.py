import streamlit as st

# Abre la cámara
video = st.camera_input()

# Muestra el video en un cuadro
st.image(video)
