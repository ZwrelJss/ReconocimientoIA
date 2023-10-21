import streamlit as st

def main():
    # Abre la cámara
    video = st.camera_input()

    # Muestra el video en un cuadro
    st.image(video)

if __name__ == "__main__":
    main()
