mausculino = 'M'
feminino = 'F'

sexo = input('Informe seu sexo (M/F): ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo (M/F): ').upper()

if sexo == 'M':
    print('Masculino!')

else:
    print('Feminino!')