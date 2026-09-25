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

#6)
print(sum(df['X'][df['X']<30]))

#7)
print(sum(df.loc['D',['W', 'X', 'Y', 'Z']])/len(df.loc['D',['W', 'X', 'Y', 'Z']]))
print(sum(df.iloc[4, ])/len(df.iloc[4, ]))

#8)
df2 = df.loc[['A','B','E'], ['X','Y']]
print(df2)

print("soma da linha A:")
print(sum(df2.loc['A', ['X','Y']]))
print("soma da linha B:")
print(sum(df2.loc['B', ['X','Y']]))
print("soma da linha C:")
print(sum(df2.loc['E', ['X','Y']]))

print("soma da coluna X:")
print(sum(df2['X']))
print("soma da coluna Y:")
print(sum(df2['Y']))