rodado = float(input('Quantos km rodados? '))

if rodado <= 200:
    total = (rodado*0.5)
else :
    total = (rodado*0.45)

print('Total a pagar é de R${:.2f}'.format(total))