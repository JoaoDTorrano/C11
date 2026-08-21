import numpy as np

# Colunas: 0=Num 1=Company Name 2=Location 3=Datum 4=Detail 5=Status Rocket 6=Cost 7=Status Mission
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

dados = dataset[1:]

empresa = dados[:, 1]
local = dados[:, 2]
detalhe = dados[:, 4]
status_foguete = dados[:, 5]
custo = dados[:, 6].astype(float)

# 6)
aposentados = status_foguete == 'StatusRetired'
print('6) Missoes com foguete StatusRetired: %.2f%%' % (len(status_foguete[aposentados]) / len(status_foguete) * 100))

# 7)
russia = np.char.find(local, 'Russia') >= 0
print('7) Missoes lancadas da Russia:', len(local[russia]))

# 8)
mais_cara = custo.argmax()
print('8) Missao mais cara do Dataset:', empresa[mais_cara], '-', detalhe[mais_cara], '-', custo[mais_cara], 'milhoes')
