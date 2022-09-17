import streamlit as st
import subprocess
import pandas as pd

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('**Coordinator**: [Danilo Andrade](https://daniloas.com/)')

estado = st.selectbox('De qual estado?', ('ES', 'BA', 'SE'))

codigo = st.text_input('Qual a letra do Código CID-10?')

dataframefinal = pd.DataFrame()
lista_totais = list()

st.subheader('1. Printing text in R')
with st.expander('See code'):
  code1 = '''print("Hello world ...")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "hello.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)


def dados():
    file = str(estado) + '.csv'
    data = pd.read_csv(file, encoding='latin-1')
    novo = pd.DataFrame(data, columns=['CAUSABAS', 'DTOBITO'])
    novo['CAUSABAS'] = novo['CAUSABAS'].astype(str)

    listaSim = []
    listaDia = []

    for i in range(0, len(novo['CAUSABAS'])):
        sim = str(novo.loc[i][0])
        dia = str(novo.loc[i][1])
        if sim[0] == codigo:
            listaSim.append(sim)
            listaDia.append(dia)
        else:
            i = i

    lista_de_tuplas = list(zip(listaSim, listaDia))
    dataframefinal = pd.DataFrame(lista_de_tuplas, columns=['CAUSABAS', 'DTOBITO'])
    dataframefinal.sort_values(['DTOBITO', 'CAUSABAS'], inplace=True, ignore_index=True)
    return dataframefinal


if st.button('Extrair dados'):
    dadosordenados = dados()
    st.write(dadosordenados)

def totais_por_ano():
    dadosordenados = dados()
    j = 0
    n = 1

    listaN = []
    listaData = []
    listaValor = []

    for i in range(0, 30):

        if dadosordenados.loc[j][1] == dadosordenados.loc[j + 1][1]:
            print('Passagem pelo elif')
            print(j)
            print(n)
            print(dadosordenados.loc[j][1])
            print(dadosordenados.loc[j + 1][1])
            n = n + 1
            j = j + 1
        else:
            print('Passagem pelo else')
            print(j)
            print(n)
            listaN.append(n)
            listaValor.append(n)
            listaData.append(dadosordenados.loc[j][1])
            n = 1
            j = j + 1
    lista_totais = list(zip(listaValor, listaData))
    dataframetotais = pd.DataFrame(lista_totais, columns=['V', 'DATA'])
    st.write(dataframetotais)
    return dataframetotais


if st.button('Totais'):
    dataframetotais = totais_por_ano()
    st.write(dataframetotais)


def convert_df(df):
    return df.to_csv().encode('utf-8')

st.download_button(
    "Baixar tabela de dados",
    convert_df(dados()),
    "file.csv",
    "text/csv",
    key='download-csv'
)
