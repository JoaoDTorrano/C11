import numpy as np
# Plantando a semente aleatoria
np.random.seed(5)
arr = np.random.randint(1,10,10)
print(arr)

#Extraindo elementos únicos
print(np.unique(arr))

#Contando elementos unicos
print(np.unique(arr, return_counts=True))