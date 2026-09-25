import numpy as np
import pandas as pd

#Como preencher uma Series
#Lista de labels
#Lista de valores

labels = ['Tiago','Mateus', 'Bruna', 'Julia']
valores = [23,25,27,22]

#Criando a Series
se1 = pd.Series(index = labels, data = valores)
print(se1)
print(type(se1))

#Acessando elementos da Series
print(se1['Mateus'])
print(se1[['Mateus', 'Julia']])
