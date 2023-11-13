import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
st.write("Yuren joshua salgado martinez")
st.write("no. control 1909141")
st.write("semestre 9")


#se casrga el dataframe y se visualiza en una grafica
df = pd.read_csv("housing.csv")
st.line_chart(df['population'])

# Agregar un control deslizante
#age = st.slider("Selecciona una edad", 0, 100, 30)

#agrega un video mediante un link
#st.video("https://www.youtube.com/watch?v=TXSOitGoINE")

#corre la pagina
#streamlit run mi_app.py