import numpy as np
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([60,40,20,10,5])
arr3 = arr1 + arr2

#Operacoes entre Arrays
print(arr3)
print(arr1 - arr2)
print(arr1 * arr2)

#Concatenacao de Arrays
arr3 = np.concatenate((arr1,arr2))
print(arr3)

#Broadcasting - quando um ESCALAR faz uma operacao com um ARRAY
arr4 = 5 * arr3
print(arr4.reshape(10,1))

# ESTRUTURANDO UMA MATRIZ COM CONTAS
mtz = np.arange(10,96,5)
mtz = mtz.reshape(3,6)

#Extraindo a soma da primeira coluna (net)
print(mtz.sum(axis=0)) # Eixo 0 = coluna
print(mtz.sum(axis=0)[0])

#Extraindo a soma da segunda linha (fev)
print(mtz.sum(axis=1)) # Eixo 0 = linha
print(mtz.sum(axis=1)[1])