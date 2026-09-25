import numpy as np

arr1 = np.arange(0,51,2)
print(arr1)
arr2 = (np.arange(-100,-49,2)*(-1))
print(arr2)
arr3 = np.concatenate((arr1, arr2))
print(arr3)