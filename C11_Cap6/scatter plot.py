import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('paises.csv', delimiter =';')
print(ds.columns)

#Quao dispersas estao as rendas per capita dos 6 paises do mundo
#pegando apenas 6 maiores paises do planeta
maioresPaises = ds.nlargest(6, 'Area (sq. mi.)')
print(maioresPaises)

#tracando o grafico com a renda per capta desses paises
#O parametro s permite adicionar uma terceira dimensao neste grafico
plt.scatter(maioresPaises['Country'],
            maioresPaises['GDP ($ per capita)'],
            maioresPaises['Population']/1000000)
plt.show()