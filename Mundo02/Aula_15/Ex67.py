'''Crie um Script em Python  que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

tabu = cont = 0
while True:
    n = int(input('Quer ver a tabuada de que numero?: '))
    cont+=1
    if n < 0:
        break
    for cont in range (1,11):
        print(f'''{cont} x {n} = {cont*n}''')

print('Até uma proxima!!!')
