'''Crie um Script em python que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano a {}ª pessoa nasceu?: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('temos {} pessoas maior de idade\ntemos {} pessoas menor de idade'.format(totmaior, totmenor))
