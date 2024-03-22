# Crie um Script em Python que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

print('digite o valor de um ângulo que eu falo para você os valores do seno, cosseno, e tangente desse ângulo.')
ângulo = int(input('digite aqui o valor do ângulo desejado: '))
a = math.radians(ângulo)
s = math.sin(a)
c = math.cosh(a)
t = math.tan(a)
print('O valor do seno é {:.2f}\n'
      'O valor do cosseno é {:.2f}\n'
      'O valor do tangente é {:.2f}\n'
      'Do ângulo {:.0f}°.'.format(s, c, t, ângulo))

# OU

from math import sin, cosh, tan, radians
print('Digite o valor de um numero qualquer.'
      '\n Que eu mostrarei o valor do Seno, Cosseno e tangente.')
Ângulo = float(input('Digite o valor do numero que vc quer saber o valor do Seno, Cosseno e Tangente: '))
num = math.radians(Ângulo)
se = sin(num)
co = cosh(num)
ta = tan(num)
print('O valor do Seno é {:.2f}, do Cosseno é {:.2f} e do Tangente é {:.2f} do Numero e {:.2f}° '.format(se, co, ta, Ângulo))
