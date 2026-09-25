import math

angulo = float(input('Digite o valor do angulo: '))
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print('cosseno de {0} é {1}, seno de {0} é {2} e tangente de {0} é {3}'.format(angulo,math.ceil(cos),math.ceil(sen),math.ceil(tg)))