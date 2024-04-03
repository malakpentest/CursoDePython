'''Crie um Script em python que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''. join(palavras)
inverso = ''
for letra in range(len(juntos)-1,-1,-1):
    inverso += juntos[letra]
if inverso == juntos:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao é um palíndromo!')
print(juntos, inverso)

# OU

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''. join(palavras)
inverso = juntos[::-1]
print('O inverso de {} é {}'.format((juntos, inverso)))
if inverso == juntos:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao é um palíndromo!')
print(juntos, inverso)
