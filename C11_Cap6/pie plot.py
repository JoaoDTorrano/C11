import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('paises.csv', delimiter =';')
print(ds.columns)

peisesSemCosta = ds[ds['Coastline (coast/area ratio)'] == 0]
print(peisesSemCosta)

qtSemcosta = len(peisesSemCosta)
qtComcosta = len(ds) - qtSemcosta

plt.pie(x = [qtSemcosta, qtComcosta], labels = ['%Paises sem Costa',
                                                '%Paises com Costa'],
        autopct='%1.1f%%')
plt.show()