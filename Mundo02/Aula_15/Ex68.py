'''Crie um script em Python que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o 
total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import choice
from time import sleep
print('=-'*30)
print('{:^60}'.format('VAMOS JOGAR PAR OU IMPAR'))
print('-='*30)
par = impar = 0

b = [1,2,3,4,5,6,7,8,9,10]
while True:
    player = int(input('Diga um valor: '))
    comput = choice(b)
    relsut = player + comput
    par =  relsut % 2 == 0
    impar= relsut % 3 == 0
    escolha = str(input('[P/I]: ')).upper()
    if escolha == 'I':
        if impar:
            print('Pensando...')
            sleep(2)
            print(f'Você venceu eu escolhi {comput} e Você escolheu {player} o resultado deu {relsut} que é impar!!!')
            print('vamos de novo')
        elif par:
            print('Pensando...')
            sleep(2)
            print(f'Você perdeu eu escolhi {comput} e Você escolheu {player} o resultado deu {relsut} que é Par!!!')
            print('Eu ganhei')
            break
    if escolha == 'P':
        if par:
            print('Pensando...')
            sleep(2)
            print(f'Você venceu eu escolhi {comput} e Você escolheu {player} o resultado deu {relsut} que é par!!!')
            print('vamos de novo')
        elif impar:
            print('Pensando...')
            sleep(2)
            print(f'Você perdeu eu escolhi {comput} e Você escolheu {player} o resultado deu {relsut} que é impar!!!')
            print('Eu ganhei')
            break
#OU

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    comp = randint(0, 11)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR?: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o PC {comp}. Total de {total}',end=' ')
    print('DEU PAR'if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você Venceu {v} Vezes.')
