import streamlit as st
import subprocess
from pysus.online_data.SIM import download

st.subheader('oiii')
with st.expander('Veja o Código'):
    code1 = '''print("Hello world!....")
    '''
    st.code(code1, language = 'R')

process1 = subprocess.Popen(["Rscript", "hello.R"],  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)



estados =['ES']
anos = [2014, 2015, 2016, 2017, 2018]
banco={}
for y in anos:
 for uf in estados:
     banco[uf, y] = download(state = uf, year=y)
     print("Banco de " + str(y) + " de " + str(uf) + " baixado!")

st.write(result1)

'''
st.subheader('teste Sus')
with st.expander('Veja o Código'):
process2 = subprocess.Popen(["Rscript", "testesus.R"],  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
st.write(result1)
'''