import numpy as np
import pandas as pd

#1)
linguagens = ['Java', 'Python', 'C']
ano1 = [16.25, 9.85, 16.04]
ano2 = [11.68, 12.12, 16.21]
seriesAno1 = pd.Series(index=linguagens, data=ano1)
seriesAno2 = pd.Series (index=linguagens, data=ano2)

#2)
print(sum(seriesAno1))
print(sum(seriesAno2))

#3)
print(seriesAno1.sub(seriesAno2))

#4)
dados = seriesAno1.sub(seriesAno2)
print(dados[dados>0])

#5)
dados2 = pow(dados, 2)
print(dados2.nlargest(1))

