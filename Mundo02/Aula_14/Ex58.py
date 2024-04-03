'''Crie um Script em Python que Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import choice
print('Bem vindo ao sorteio Fefe da Sorte')
n = int(input('Digite um numero de 1 a 10: '))
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolido = choice(b)
palpite = 0
while n != escolido:
    n = int(input('Tente novamente: '))
    palpite += 1
    if n < escolido:
        print('tente novamente o numero e maior! ')
    elif n > escolido:
        print('Tente novamente o numero e menor! ')
print('Você acertou com {} tentativas o numero escolhido foi {}!!!'.format(palpite, escolido))

#OU

from random import randint
comp = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qua é seu palpite?: '))
    palpite += 1
    if jogador == comp:
        acertou= True
    else:
        if jogador < comp:
            print('É maior ... Tente mais uma Vez.')
        elif jogador > comp:
            print('É menor... Tente mais uma vez.')
print('Você acertou!!! com {} tentativas Parabéns'.format(palpite))
