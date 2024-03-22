# Crie um Script em Python que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input('Digite um número: ')).strip()
print('Analisando o número {}'.format(num))
print('A unidade desse número é {}'.format(num[3]))
print('A dezena desse  número é {}'.format(num[2]))
print('A centena desse número é {}'.format(num[1]))
print('A milhar desse número é {}'.format(num[0]))

# OU

num = int(input('Digite o valor do numero: '))
n = str(num)
print('Analizando o número {}'.format(n))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('milhar: {}'.format(n[3]))

# OU

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}'.format(num))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
