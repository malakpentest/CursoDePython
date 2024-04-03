'''Crie um Script em Python que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n ,f))

#OU

from time import sleep
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
sleep(2)
while c > 0:
    print('{}'.format(c),end='')
    print(' x 'if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))

#OU

from time import sleep
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
sleep(2)
for c in range(c, 0, -1):
    print('{}'.format(c),end='')
    print(' x 'if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))
