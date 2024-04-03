'''Crie um Scrip em python que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

print('_-'*30)
print('{:^60}'.format('BEM VINDO A CALCULADORA FEFE'))
print('_-'*30)
núm = soma = cont = 0
print('Voce pode digitar 999 para parar')
núm = int(input('Digite um Valor: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um valor: '))
print('_-'*30)
print('Você digitou {} numeros e a soma desses numeros e {} .'.format(cont, soma))
print('_-'*30)
