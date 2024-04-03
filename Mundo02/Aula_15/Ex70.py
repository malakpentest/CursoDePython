'''Crie um Script em Python que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''


print('-'*30)
print(f'{"LOJA DA VEVIS":^30}')
print('-'*30)
total = cont = totmil  = menor = 0
mbarato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        mbarato = nome
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print('-'*11,end='')
print(f'{" FIM DO PROGRAMA "}',end='')
print('-'*11)
print(f'Total gasto na compra R$:{total:.2f}\nTemos {totmil} produto custando mais que R$:1000.00\nO produto mais barato é → {mbarato} que custa {menor} ')

#OU

totp = mais = mpreço = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    totp += preço
    if preço > 1000:
        mais += 1
    if cont == 1 or preço < mpreço:
        mpreço = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] :')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total gasto foi de R$:{totp:.2f}')
print(f'Tem {mais} que custa mais que R$ 1000,00 Reais')
print(f'O produto mais barato e {barato} que custa {mpreço}')
print(f'{"FIM DO PROGRAMA":-^40}')
