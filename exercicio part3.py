import numpy as np

# Colunas: 0=Num 1=Company Name 2=Location 3=Datum 4=Detail 5=Status Rocket 6=Cost 7=Status Mission
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

dados = dataset[1:]

empresa = dados[:, 1]
local = dados[:, 2]
detalhe = dados[:, 4]
status_foguete = dados[:, 5]
custo = dados[:, 6].astype(float)
status_missao = dados[:, 7]

# 1)
sucesso = status_missao == 'Success'
print('1) Missoes bem sucedidas: %.2f%%' % (len(status_missao[sucesso]) / len(status_missao) * 100))

# 2)
com_valor = custo[custo > 0]
print('2) Media de gastos: %.2f milhoes' % (com_valor.sum() / len(com_valor)))

# 3)
eua = np.char.find(local, 'USA') >= 0
print('3) Missoes dos EUA:', len(local[eua]))

# 4)
spacex = empresa == 'SpaceX'
custo_spacex = custo[spacex]
detalhe_spacex = detalhe[spacex]
mais_cara = custo_spacex.argmax()
print('4) Missao mais cara da SpaceX:', detalhe_spacex[mais_cara], '-', custo_spacex[mais_cara], 'milhoes')

# 5)
empresas, quantidades = np.unique(empresa, return_counts=True)
print('5) Missoes por empresa:')
for nome, qtd in zip(empresas, quantidades):
    print('   ', nome, '->', qtd)
