import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Plotando graficos de linhas com matplotlib(Plot)
x = np.array([1,2,3,4])
y =x*2
y2 = x**2

#Quando se cria um subplot, deve se passar quantas linhas e quantas colunas tem a grade subplots)
plt.subplot(1,2,1)
plt.plot(x, y, '*:r',linewidth = '3', markersize = 20)
#legendas nos eixos x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')


plt.subplot(1,2,2)
plt.plot(x, y2, 's--b', linewidth = '3', markersize = 20)
#legendas nos eixos x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.show()