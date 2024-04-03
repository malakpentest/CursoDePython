'''Crie um Script em Python que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''



pnum = int(input('Digite um Numero: '))
snum = int(input('Digite o segundo Numero: '))
c = [1, 2, 3, 4, 5]
r = 0
while r != 5:
    print('''escolha uma opção
    [1] soma
    [2] mutiplicação
    [3] saber qual e o maior
    [4] inserir novos numeros
    [5] sair ''')
    r = int(input('qual opção você escolhe: '))
    if r == 1 :
        print(' {} + {} = {}'.format(pnum,snum, snum+pnum))
    if r == 2 :
        print('{} x {} = {}'.format(pnum, snum, pnum*snum))
    if r == 3 :
        if pnum > snum:
            print('entre o numero {} e {} o numero {} e maior '.format(pnum, snum, pnum))
        elif snum > pnum:
            print('entre os numeros {} e {} o numero {} e maior'.format(pnum, snum, snum))
    if r == 4 :
        pnum = int(input('Digite um Numero: '))
        snum = int(input('Digite o segundo Numero: '))
        print('''escolha uma opção
            [1] soma
            [2] mutiplicação
            [3] saber qual e o maior
            [4] inserir novos numeros
            [5] sair ''')
        r = int(input('qual opção você escolhe: '))
        if r == 1:
            print(' {} + {} = {}'.format(pnum,snum, snum+pnum))
        if r == 2:
            print('{} x {} = {}'.format(pnum, snum, pnum*snum))
        if r == 3:
            if pnum > snum:
                print('entre o numero {} e {} o numero {} e maior '.format(pnum, snum, pnum))
            elif snum > pnum:
                print('entre os numeros {} e {} o numero {} e maior'.format(pnum, snum, snum))
        else:
            print('Opção invalida tente novamente !!!')
    else:
        print('Opção invalida tente novamente !!!')
print('Obrigado ate mais !')

OU

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] digite outro numeros
    [ 5 ] Sair''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2 :
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('informe os nùmeros novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor'))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invàlida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
