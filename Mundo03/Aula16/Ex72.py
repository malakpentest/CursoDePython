#Desafio 72
lista = ('zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove'
         , 'Dez', 'Onze', 'Doze', 'Treze', 'Quartorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
r = 0

while True:
    resposta = int(input('Digite um valor entre 0 a 20: '))
    if 0 <= resposta <= 20:
        print('você digitou o numero {}'.format(lista[resposta]))
        print('quer continuar?\n1 SIM 2 NÃO')
        r = int(input('1 ou 2: '))
        if r == 2:
            print('Obrigado até uma proxima!!!')
            break
        if r == 1:
            print('Ok vamos là!!!')
        else:
            print('resposta invalida tente novamente!!!')
            break
    else:
        print('Resposta invalida tente novamente ENTRE O NUMEROS 0 AO 20!!!:  ')

#ou
lista = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove'
         , 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
         'Vinte')

while True:
    núm = int(input('Digite um valor entre 0 a 20: '))
    if 0 <= núm <= 20:
        print('Tente novamente {}',end='')
        print(f'Você digitou o numero {lista[núm]}')
    print('Você quer continuar?\n1 Sim 2 Não')
    r = int(input('continuar?: '))
    if r == 2:
        print('Obrigado volte sempre!!!')
        break

