import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2}'.format(num, raiz))
#print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) [arredonda para baixo]
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))  [arredonda para cima}