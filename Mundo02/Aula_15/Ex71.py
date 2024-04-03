'''Crie um Script em Python que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
 e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=-'*15)
print(f'{"BANCO DO FEFE":^30}')
print('=-'*15)
valor = float(input('qual e o valor que Você deseja sacar? : R$'))
total = valor
ced = 50
totalced = 0
resp = ' '
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedula de R$:{ced}')
        if ced == 50:
           ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            print('Obrigado tenha um otimo dia até uma proxima!')
            break
