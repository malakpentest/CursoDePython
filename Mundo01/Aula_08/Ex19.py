# Crie um Script em Python que ajude um professor a sortear um dos seus quatro alunos para apagar o quadro.

import random
print('Olá, aluno Bem vindo ao sorteio da class ')
a1 = str(input('Digite seu nome aluno: '))
a2 = str(input('Digite seu nome aluno: '))
a3 = str(input('Digite seu nome aluno: '))
a4 = str(input('Digite seu nome aluno: '))
lista = [a1, a2, a3, a4]
print('Lista de alunos concorrendo \n'
'1 ) - {:=^20} \n'
'2 ) - {:=^20} \n'
'3 ) - {:=^20} \n'
'4) - {:=^20} '.format(a1, a2, a3, a4))
print('Agora é a hora você esta pronto?')
r = bool(input('digite S/N: '))
num = random.choice(lista)
print('parabens {} voce acaba de ganhar !!!'.format(num))

# OU

from random import choice
print('Olá, Bem vindo ao Sorteio de aluno da class')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno :')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
escolido = choice(lista)
print('Parabens {} voce acaba de ganhar'.format(escolido))
