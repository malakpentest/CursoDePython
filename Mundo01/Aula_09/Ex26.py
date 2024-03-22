''' Crie um Script em Python que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. '''

frase = str(input('Digite uma frase: ')).strip()
l = frase.upper()
print('A letra (a) aparece {} vezes na frase "{}"'.format(l.count('A'),frase))
print('A primeira letra (a) foi encontrada na {}° letras'.format(l.find('A')+1))
print('A ultima Letra (a) foi encontrada na {}° da frase'.format(l.rfind('A')+1))
