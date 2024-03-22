#Crie um Script em Python que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimeto do cateto adjacentes: '))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# OU

import math
print('Olá, para você saber o valor da hipotenusa digite a baixo as seguintes informação:')
co = float(input('digite o valor do cateco oposto (altura): '))
ca = float(input('digite o valor do cateto adjacente (largura): '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))

# OU

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto abjacente: '))
hi = hypot(ca, co)
print('O valor da hipotenusa do valores {}, e {} são {:.2f}.'.format(co, ca, hi))
