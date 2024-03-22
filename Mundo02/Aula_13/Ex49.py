''' Crie um Script em Python que Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

n = int(input('Digite a tabuada que vc quer: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, n*c))
