valor_metros = float(input('Valor em metros: '))
valor_centimetros = valor_metros * 100
valor_melimetros = valor_metros * 1000

print('{}m é igual a {:.2f}cm e a {:.2f}mm'.format(valor_metros, valor_centimetros, valor_melimetros))