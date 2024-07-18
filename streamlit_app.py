import streamlit as st

# Definir la función que convierte el texto a mayúsculas
def convertir_a_mayusculas(texto):
    return texto.upper()

# Título de la aplicación
st.title("Aplicación de Conversión a Mayúsculas")

# Cuadro de texto para que el usuario ingrese el texto
texto_ingresado = st.text_input("Ingresa el texto aquí:")

# Botón para realizar la conversión
if st.button("Convertir a Mayúsculas"):
    # Verificar si se ha ingresado texto
    if texto_ingresado:
        texto_convertido = convertir_a_mayusculas(texto_ingresado)
        # Mostrar el texto convertido en un área de texto
        st.text_area("Texto en Mayúsculas:", value=texto_convertido, height=200)
    else:
        st.error("Por favor, ingresa un texto.")
