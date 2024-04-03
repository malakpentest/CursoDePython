'''Crie um Script em Python que lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA')
print('-=' *10)
pnum = int(input('Digite o primeiro termo: '))
snum = int(input('Digite a razão da PA: '))
print('-='*10)
termo = 0
cont = 1
while cont <= 10:
    print('{} → '.format(termo),end='')
    termo += snum
    cont +=1
print('FIM')
