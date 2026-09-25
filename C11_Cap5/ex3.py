import numpy as np
import pandas as pd

ds = pd.read_csv('paises.csv', sep=';')

#1)
# Os valores de Region e Country vêm com espaços sobrando no fim
ds['Region'] = ds['Region'].str.strip()
ds['Country'] = ds['Country'].str.strip()

print(ds.columns)

paises_oceania = ds[ds['Region'] == 'OCEANIA']['Country']
print(paises_oceania)

print('Número de países da Oceania:', paises_oceania.count())

#2)
(print(ds.nlargest(1, ['Population'])[['Region', 'Country']]))

#3)
paises_regiao = ds.groupby('Region')
print(paises_regiao['Literacy (%)'].sum() / paises_regiao['Literacy (%)'].count())

#4)
noCoast = ds[ds['Coastline (coast/area ratio)'] == 0]['Country']
print(noCoast)
noCoast.to_csv('noCoast.csv', index=False)

#5)
def deathInd (x):
    if x < 9:
        return 'Balanced'
    else:
        return 'Urgent'

ds['Humanitarian Help'] = ds['Deathrate'].apply(deathInd)
print(ds)





