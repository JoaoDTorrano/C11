import math
coop = float(input('Comprimento do cateto oposto: '))
coad= float(input('Comprimento do cateto adjacente: '))

hip = math.hypot(coop,coad)
#hip = math.sqrt((coop**2) + (coad**2))

print('O valor da hipotenusa é {:.2f}'.format(hip))