''' Crie um Script em Python que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import choice
print('Bem vindo ao sorteio Fefe da Sorte')
n = int(input('Digite um numero de 1 a 10: '))
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolido = choice(b)
if n == escolido:
    print('parabens você ganhou!!!')
else:
    print(' nao foi dessa vez!!!')
print('obrigado por participar o numero escolhido foi {}!!!'.format(escolido))

# OU

from random import randint
from time import sleep
computador = randint(0,10) # fazer o computador escolher
print('><_><=-'*20)
print('Vou escolher um número entre 0 e 10 tente adivinhar...')
print('><_><=-'*20)
jogador = int(input('Qual foi o numero que eu pensei?'))
print('PROCESSANDO...')
sleep(5)
if jogador == computador:
    print('PARABENS!!! você acertou!!!')
else:
    print('HAHAHA não foi dessa vez.. eu escolhi {} e você falou {}!'.format(computador, jogador))
