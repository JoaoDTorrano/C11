import numpy as np
import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')

#6)
paises_regiao = ds.groupby('Region')
populacao_regiao = paises_regiao['Population']
descricao_populacao = populacao_regiao.describe()
print(descricao_populacao)
print(descricao_populacao.head(5))

#7)
def infantMred (x):
    return x*0.85

original = ds['Infant mortality (per 1000 births)']
meta = original.apply(infantMred)
meta.name = 'Infant mortality goal (-15%)'

comparacao = pd.concat([original, meta], axis=1)
print(comparacao)

