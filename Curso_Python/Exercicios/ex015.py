dia = int(input('Quantos dias alugados? '))
rodado = float(input('Quantos km rodados? '))

total = (dia*60) + (rodado*0.15)

print('Total a pagar é de R${:.2f}'.format(total))