lista = ('Caneta','Lapis','Borracha','Apontador','Caderno','Agenda','Revista','Compasso','Estojo','Mochila','Regua')
a = 'a'
for c in lista:
    print(f'\nNa palavra {c.upper()} temos ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
