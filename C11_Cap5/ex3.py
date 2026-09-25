import numpy as np
import pandas as pd

ds= pd.read_csv('paises.csv', sep = ';')

print(ds.columns)
paises_oceania = ds[ds['Region'] == 'OCEANIA']['Country']
print(paises_oceania)