import numpy as np
import pandas as pd

ds = pd.read_csv('paises.csv', sep = ';')

#6)
paises_regiao = ds.groupby('Region')
populacao_regiao = paises_regiao['Population']
descricao_populacao = populacao_regiao.describe()
print(descricao_populacao)
print(descricao_populacao.head(5))

