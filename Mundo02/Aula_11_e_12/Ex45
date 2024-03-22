# Crie um Script em Pythonque faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('><_><=-'*5)
print('vamos jogar jokenpô?')
print('><_><=-'*5)
r = int(input('''Escolha uma opção:
[ 1 ] Sim
[ 2 ] Não
:'''))
if r == 1:
    itens = ('Pedra','Papel','Tesoura')
    computador = randint (0,2)  # fazer o computador escolher
    print('O computador escolheu {}'.format(itens[computador]))
    jogador = int(input('''escolha uma opção:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    : '''))
    print('-='* 11)
    print('Jo')
    sleep(0.5)
    print('ken')
    sleep(0.5)
    print('Pô!!!')
    sleep(0.5)
    print('O computador escolheu {}'.format(itens[computador]))
    print('Voce jogou {}'.format(itens[jogador]))
    print('-='* 11)
    sleep(0.5)
    if computador == 0:
        if jogador == 0:
            print('deu empate vc jogou {} e eu joguei {}'.format(itens[jogador],itens[computador]))
        elif jogador == 1:
            print('Voce ganhou!!! vc jogou {} e eu joguei {}'.format(itens[jogador],itens[computador]))
        elif jogador == 2:
            print('Eu Ganhei!!! vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        else:
            print('jogada invalida')

    elif computador == 1:
        if jogador == 1:
            print('deu empate vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        elif jogador == 2:
            print('Voce ganhou!!! vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        elif jogador == 0:
            print('Eu Ganhei!!! vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        else:
            print('jogada invalida')

    elif computador == 2:
        if jogador == 2:
            print('deu empate vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        elif jogador == 0:
            print('Voce ganhou!!! vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        elif jogador == 1:
            print('Eu Ganhei!!! vc jogou {} e eu joguei {}'.format(itens[jogador], itens[computador]))
        else:
            print('jogada invalida')


elif r == 2:
    print('O brigado, volte quando quiser jogar!!!')
else:
    print('opção invalida!!!')

