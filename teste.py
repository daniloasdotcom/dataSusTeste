import pandas as pd

file = str('ES') + '.csv'
data = pd.read_csv(file, encoding='latin-1')
novo = pd.DataFrame(data, columns=['CAUSABAS', 'DTOBITO'])
novo['CAUSABAS'] = novo['CAUSABAS'].astype(str)

listaSim = []
listaDia = []


def dados():
    for i in range(0, len(novo['CAUSABAS'])):
        sim = str(novo.loc[i][0])
        dia = str(novo.loc[i][1])
        if sim[0] == 'E':
            listaSim.append(sim)
            # print('Valor de SIM')
            # print(sim)
            listaDia.append(dia)
            # print('Valor de dia')
            # print(dia)
        else:
            i = i
            # print('Valor de i')
            # print(i)

    lista_de_tuplas = list(zip(listaSim, listaDia))
    dataframefinal = pd.DataFrame(lista_de_tuplas, columns=['CAUSABAS', 'DTOBITO'])
    print(dataframefinal.head())

    dataframefinal.sort_values(['DTOBITO', 'CAUSABAS'], inplace=True, ignore_index=True)
    # print(dataframefinal02.head())

    return dataframefinal

dadosordenados = dados()

print(dadosordenados)


def totais_por_ano():
    dadosordenados = dados()
    print('oi')
    print(dadosordenados.head(15))
    j = 0
    n = 1

    listaN = []
    listaData = []
    listaValor = []

    for i in range(0, len(dadosordenados['CAUSABAS'])):

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
    print('final')
    print(dataframetotais)


totais_por_ano()


"""
st.subheader('1. Printing text in R')
with st.expander('See code'):
  code1 = '''print("Hello world ...")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "hello.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)

process2 = subprocess.Popen(["Rscript", "fetch_datasus.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if st.button('Extrair dados'):
    dadosordenados = process2.communicate()
    st.write(dadosordenados)
"""