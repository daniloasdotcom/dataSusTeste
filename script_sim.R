codigo = readline(prompt="Entre com o Código: ")

# Instalando o pacote para coleta e pre-processamento de dados do DATASUS
# Necessario para corrigir problemas com Windows 10

Sys.setenv(R_REMOTES_STANDALONE="true") 

remotes::install_github("rfsaldanha/microdatasus")
library(microdatasus)
library(writexl)

# Extraindo os dados de mortalidade
sim.es <- fetch_datasus(year_start = 2020, 
                        month_start = 1, 
                        year_end = 2020, 
                        month_end = 12, 
                        uf = "ES", 
                        information_system = "SIM-DO")

sim.es <- process_sim(sim.es)

View(sim.es)

dados = data.frame(sim.es)

setwd("C:/Users/Usuário/Desktop")
write.csv(dados, "my_df.csv")
write_xlsx(dados, 'dados.xslsx')

# Investiga o tipo de dados de CAUSABAS
typeof(sim.es$CAUSABAS)

# Uma olhada melhor sobre a estruturda de CAUSABAS
str(sim.es$CAUSABAS)

# Convertendo a causa base para fator
sim.es$CAUSABAS = as.factor(sim.es$CAUSABAS)

# E agora qual a estrutura de CAUSABAS?
str(sim.es$CAUSABAS)

# Resumo dos dados
summary(sim.es$CAUSABAS)

# Cria um novo dataframe com as informações que desejamos
novo = data.frame(sim.es$CAUSABAS, sim.es$DTOBITO)

head(novo)

typeof(novo$sim.es.CAUSABAS)
typeof(novo$sim.es.DTOBITO)

novo$sim.es.CAUSABAS = as.character(novo$sim.es.CAUSABAS)

j =  1

lista.e = c()
lista.o = c()

for (i in 1:length(novo$sim.es.CAUSABAS)) {
  
  if (substr(novo[i,1], 1, 1) == codigo) {
  
    print(paste("Identificação: ", novo[i,1]))
    lista.e[j] = novo[i,1]
    lista.o[j] = novo[i,2]
    lista.n[j] = j
    j =  j + 1
    
  } else {
    
  }
  
}

lista.e[1]
lista.o[2]
lista.n[2]

dados.e = data.frame(lista.e, lista.o)

dados.e$lista.e[2]

names(dados.e)

typeof(dados.e$lista.e)
typeof(dados.e$lista.o)

head(dados.e,20)


dados.e = dados.e[order(dados.e$lista.o),]
head(dados.e,20)

i = 1
j = 1
n = 1
f = 1

lista.n = c()
lista.data = c()
lista.valor = c()

for (i in 1:length(dados.e$lista.e)){
  
  if (j == 1){
    
    print('Passei pelo if')
    print(paste('valor de j:', j))
    lista.n[j] = n
    print(lista.n)
    j = j + 1
    n = n + 1
    
  } else if (dados.e[i,2] == dados.e[i+1,2]) {
    
    print('Passei pelo else if')
    print(paste('valor de j:', j))
    lista.n[j] = n
    j = j + 1
    n = n + 1
    
  } else {
    
    print('Passei pelo else')
    lista.n[j] = n
    lista.valor[f] = n
    lista.data[f] = dados.e[i,2]
    f = f + 1
    j = j + 1
    n = 1
    
  }
  
}

lista.data
lista.valor

tabela = data.frame(lista.data, lista.valor)
tabela$lista.data= as.Date(tabela$lista.data)

tabela$lista.data = format(tabela$lista.data, format ="%Y")



head(tabela, 30)

length(tabela$lista.valor[tabela$lista.data == '2012'])

plot(tabela$lista.data, tabela$lista.valor)

head(dados.e,20)

lista.n[7]

length(lista.n)

dados.e[8, 2] == dados.e[8-1, 2]

head(dados.e)

View(sim.es)