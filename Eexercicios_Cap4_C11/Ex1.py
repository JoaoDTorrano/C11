import numpy as np

arr1 = np.ones(8)
print(arr1)
arr2 = np.random.randint(0,9,8)
print(arr2)
arr3 = arr1 + arr2
print(arr3)

soma = np.sum(arr3)
print(soma)

if soma >= 40:
    mtz = arr3.reshape(4,2)
    print(mtz)
else:
    mtz = arr3.reshape(2,4)
    print(mtz)