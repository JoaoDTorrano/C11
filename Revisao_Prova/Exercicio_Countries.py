import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding= 'utf-8')
#1)
infos = dataset[1:, 0:4]
print(infos)


dados = dataset[1:]
pais = dados[:, 0]
regiao = dados[:, 1]
populacao = dados[:, 2].astype(int)
area = dados[:, 3].astype(int)

#2)
print(len(np.unique(regiao)))

#3)
letramento = dados[:, 9].astype(float)
alfabe_planeta = round(np.average(letramento),2)
print(alfabe_planeta)

#4)
america_norte = np.char.find(regiao, 'NORTHERN AMERICA') >=0
print(len(pais[america_norte]))

#5)
pib = dados[:, 8].astype(float)
latam_caribe = np.char.find(regiao, 'LATIN AMER. & CARIB') >= 0
pais_latam_caribe = pais[latam_caribe]
pib_latam_caribe = pib[latam_caribe]
maior_pib_latam_caribe = pib_latam_caribe.argmax()
print(pais_latam_caribe[maior_pib_latam_caribe])