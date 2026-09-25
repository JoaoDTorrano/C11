real = float(input('Digite o valor em real que deseja em dolar: '))
taxa_conversao = 3.27
dolar = real/taxa_conversao


print('R${} pode comprar US${:.2f}'.format(real,dolar))