import numpy as np
import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')
#print(ds)

#visualizando as colunas
#print(ds.columns)

#Extraindo regsitros do topo
#print(ds.head(5))

#Extraindo registros da base
#print(ds.tail(3))

#SLICING no dataset pandas
print(ds[['Region', 'Climate', 'Service']])

#Criando novos arquivos com pandas
#Calculando a porcentagem da populacao de cada pais:

#calculando a populacao total do planeta
total_population = np.sum(ds['Population'])
print(total_population)

#calculando a porcentagem de cada pais
seriesPorcPaises = (ds['Population']/total_population)*100
print(seriesPorcPaises)

#Adicionar esta Series no Dataset
ds['% Population'] = np.round(seriesPorcPaises, 3)

#Criando uma v2 do Dataset com coluna nova
ds.to_csv('paises_v2.csv')

#Pegando os 5 paises com maiores porcentagens populacionais(nlargest)
print(ds.nlargest(5, '% Population')['Country'])
#Pegando os 5 paises com menores porcentagens populacionais(nsmallest)
print(ds.nsmallest(5, '% Population')['Country'])

#AGRUPAMENTO DE DADOS(obs: só funciona se o dataset tiver ao menos uma coluna de dados categóricos)

#agrupando por regiao
group_region = ds.groupby('Region')

#paises por  regiao
print(group_region.count()['Country'])

#somando a populacao de cada regiao
group_region = ds.groupby('Region')
print(group_region.sum()['Population'])

#Criacao e aplicacao de funcoes customizadas com o pandas

#Criando uma funcao python
#funcao para dar 10% de desconto em alguma coisa
def tenPorcent (x):
    return x * 0.9

#Buscando a taxa de mortalidade de um pais
#print(ds.columns)

taxa_mortalidade = ds['Deathrate']
print(taxa_mortalidade)

ds['Deathrate - 10%'] = taxa_mortalidade.apply(tenPorcent)

print(ds.head(2))

