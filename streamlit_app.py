def convertir_a_mayusculas(texto):
    return texto.upper()

st.title("Aplicación de Conversión a Mayúsculas")

texto_ingresado = st.text_input("Ingresa el texto aquí:")

if st.button("Convertir a Mayúsculas"):
    texto_convertido = convertir_a_mayusculas(texto_ingresado)
    st.text_area("Texto en Mayúsculas:", value=texto_convertido, height=200)
