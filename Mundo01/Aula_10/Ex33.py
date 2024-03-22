# Crie um Script em Python que leia três números e mostre qual é o maior e qual é o menor.

a = float(input('digite o primeiro valor: '))
b = float(input('digite o segundo valor: '))
c = float(input('digite o terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
