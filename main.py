import streamlit as st
import subprocess

st.subheader('oiii')
with st.expander('Veja o Código'):
    code1 = '''print("Hello world!....")
    '''
    st.code(code1, language = 'R')

process1 = subprocess.Popen(["Rscript", "hello.R"],  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)