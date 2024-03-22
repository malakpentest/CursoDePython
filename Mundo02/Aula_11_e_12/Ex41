'''Crie um Script em Python para ajudar a Confederação Nacional de Natação ela precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:'''

from datetime import date
ano = date.today().year
r = int(input('Digite qual ano você nasceu: '))
if ano - r <= 9:
    print('voce tem {} anos e um nadador MIRIM'.format(ano-r))
elif ano - r <= 14:
    print('voce tem {} anos e um nadador INFANTIL!'.format(ano-r))
elif ano - r <= 19:
    print('voce tem {} anos e um nadador JUNIOR!'.format((ano-r)))
elif ano - r <= 25:
    print('voce tem {} anos e um nadador SÊNIOR!'.format(ano-r))
elif ano - r > 25:
    print('voce tem {} anos e um nadador MASTER!'.format(ano-r))
