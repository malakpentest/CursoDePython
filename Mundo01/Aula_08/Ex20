# Crie um Script em Python que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
print('Olá, aluno Bem vindo ao sorteio da class ')
a1 = input('Digite seu nome aluno: ')
a2 = input('Digite seu nome aluno: ')
a3 = input('Digite seu nome aluno: ')
a4 = input('Digite seu nome aluno: ')
lista = [a1, a2, a3, a4]
print('Lista de alunos concorrendo \n 1 ) - {:=^20} \n 2 ) - {:=^20} \n 3 ) - {:=^20} \n 4) - {:=^20} '.format(a1, a2, a3, a4))
print('Agora é a hora você esta pronto?')
r = bool(input('digite S/N: '))
num = random.shuffle(lista)
print('parabens {} voce acaba de ganhar !!!'.format(lista))

# OU

from random import shuffle
print('Bem vindo, ao sorteio da class')
a1 = input('digite o primeiro aluno: ')
a2 = input('degite o segundo aluno: ')
a3 = input('digite o terceiro aluno: ')
a4 = input('digite o quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A classificação da lista ficou assim ')
print(lista)
