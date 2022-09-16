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



st.subheader('teste Sus')
with st.expander('Veja o Código'):
    code1 = '''print("Hello world!....")
    '''
    st.code(code1, language = 'R')

process2 = subprocess.Popen(["Rscript", "testesus.R"],  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
st.write(result1)