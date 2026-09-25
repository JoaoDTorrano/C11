x = int(input('Digite um numero: '))
a = int(input('Digite o range da tabuada: '))

for c in range (1,a+1):
    resultado = x * c
    print('A tabuada de {} é:'.format(x))
    print('{} * {} = {}'.format(x,c,resultado))
