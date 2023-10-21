import streamlit as st
import cv2

def main():
    st.title("Aplicación de Transmisión de Cámara")

    cap = cv2.VideoCapture(0)  # Abre la cámara predeterminada (0) o una cámara específica (p. ej., 1, 2)

    if not cap.isOpened():
        st.error("No se pudo abrir la cámara.")
        return

    st.write("Presiona el botón para iniciar la transmisión:")

    if st.button("Iniciar transmisión"):
        st.write("Transmisión en vivo:")
        run = True
        while run:
            ret, frame = cap.read()
            if not ret:
                st.error("Error al capturar el cuadro de la cámara.")
                break

            # Mostrar el cuadro de la cámara en Streamlit
            st.image(frame, channels="BGR", use_column_width=True)

            if not st.checkbox("Mostrar video en vivo"):
                run = False

    # Liberar la cámara al final
    cap.release()

if __name__ == "__main__":
    main()
