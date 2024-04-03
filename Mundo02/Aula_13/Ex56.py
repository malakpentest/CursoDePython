'''Crie um Script em Python  que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelhor = ''
totmulher20 = 0
for p in range(0, 4):
    print('=-=-=-ALISTAMENTO=-=-=-=')
    n = str(input('Digite seu nome: '))
    i = int(input('Digite sua idade: '))
    print('1 - Homem\n'
          '2 - Mulher')
    s = int(input('Digite seu sexo: '))
    if s == 1:
        h = s
    if s == 2:
        m = s
    somaidade += i
    if p == 1 and h :
        maioridadehomem = i
        nomevelhor = n
    if h in '1' and i > maioridadehomem:
        maioridadehomem = i
        nomevelhor = n
    if m in '2' and i < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo éa de {.:1f} anos'.format(mediaidade))
print('O homem mais velhor tem {} anos e se chama {}.'.format(maioridadehomem, nomevelhor))
print('Ao total de mulheres com menos de 20 anos {}.'.format(totmulher20))
