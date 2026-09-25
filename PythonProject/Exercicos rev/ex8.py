n1 = float(input('n1 = '))
n2 = float(input('n2 = '))

r1 = n1 + n2
r2 = n1 - n2
r3 = n1 * n2
r4 = n1 / n2
r5 = n1 ** n2
r6 = n1 // n2
r7 = n1 % n2

print('{} mais {} é igual a {} '.format(n1, n2, r1) , '\n'
      '{} menos {} é igual a {} '.format(n1, n2, r2) , '\n'
      '{} multiplicado por {} é igual a {} '.format(n1, n2, r3) , '\n'
      '{} dividido por {} é igual a {:.3f} '.format(n1, n2, r4) , '\n'
      '{} elevado a {} é igual a {} '.format(n1, n2, r5) , '\n'
      '{} dividido inteiramente {} é igual a {} '.format(n1, n2, r6) , '\n'
      '{} resto da divisão {} é igual a {} '.format(n1, n2, r7))