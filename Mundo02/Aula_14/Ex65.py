'''Crie um Script em python que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.'''

print('#-'*30)
print('{:^60}'.format('BEM VINDO'))
print('#-'*30)
continuar = 'S'
soma = maior = menor = média = cont = n1 = 0
while continuar in 'S':
    n1 = int(input('Digite um número: '))
    soma += n1
    cont += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = str(input('Quer continuar? [S/N]?: ')).upper().strip()[0]
    média = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont,média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Até Mais!!')
