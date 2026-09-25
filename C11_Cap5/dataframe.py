import numpy as np
import pandas as pd

#Como preencher uma dataframe
#Lista de labels(Colunas)
colunas = ['W', 'X', 'Y', 'Z']
#Lista de labels(linhas)
linhas = ['A', 'B', 'C', 'D', 'E']

np.random.seed(10)

#Lista de valores
valores = np.random.randint(1,50,[5,4])

df = pd.DataFrame(columns=colunas, index=linhas, data=valores)
print(df)

#Maniulando o Dataframe
# Puxando uma unica coluna do DataFrame
print(df['X'])

#Puxando uma unica celula
print(df['Y']['C'])

#Puxando multiplas colunas
print(df[['W','X', 'Z']])

#LOC & ILOC

#Puxando uma unica linha no dataframe
print(df.loc['C',['W','X', 'Y', 'Z']])
print(df.iloc[2, :])

#Puxando multiplas linhas
print(df.loc[['B','E'],['W','X', 'Y', 'Z']])
print(df.iloc[[1,4], :])


