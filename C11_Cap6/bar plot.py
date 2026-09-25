import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('paises.csv', delimiter =';')
print(ds.columns)

#qual a diferenca das 5 maiores rebdas per capita do dataset
maioresGDP = ds.nlargest(5, 'GDP ($ per capita)')
print(maioresGDP)

plt.bar(maioresGDP['Country'], maioresGDP['GDP ($ per capita)'])
plt.show()