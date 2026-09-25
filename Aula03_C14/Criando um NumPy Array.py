#Criando um NumPy Array
#import o NumPy
import numpy as np

#Criando um NumPy Array 1D
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
print(type(arr))
#propriedades do Array
print(arr.size)
print(arr.ndim)
print(arr.shape)

mtz = np.array([[10,20], [30,40], [50,60]])
print(mtz)
#propriedades do Array
print(mtz.size)
print(mtz.ndim)
print(mtz.shape)

