import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
st.write("Yuren joshua salgado martinez")
st.write("no. control 1909141")


df = pd.read_csv("datos.csv")
st.line_chart(df)