# Desafio 73
lista = ('Flamengo',
'Palmeiras SP',
'Botafogo FR RJ',
'Bahia',
'CA Paranaense PR',
'São Paulo FC SP',
'Cruzeiro',
'Fortaleza CE',
'Red Bull Bragantino SP',
'Internacional RS',
'Atletico Mineiro MG',
'EC Juventude RS',
'Criciúma',
'Cuiabá Esporte Clube MT',
'EC Vitória BA',
'Vasco Gama',
'AC Goianiense GO',
'Gremio',
'Corinthians SP',
'Fluminense RJ')
print('=-'*30)
print('{:^60}'.format('CAMPEONATO BRASILEIRO'))
print('-='*30)
print('')
for classi in enumerate(lista):
    print('{}° {}'.format(classi[0]+1,classi[-1]))
print('')
print('-='*30)
print('{:^60}'.format('OS 5 PRIMEIRO COLOCADO'))
print('-='*30)
print('')
for cl in enumerate(lista[0:5]):
    print('{}° {}'.format(cl[0]+1,cl[-1]))
print('')
print('-='*30)
print('{:^60}'.format('OS 4 ULTIMOS COLOCADO'))
print('-='*30)
print('')
for ult in lista[-4:]:
    print(ult)
print('')
print('-='*30)
print('{:^60}'.format('OS TIMES EM ORDEM ALFABETICA'))
print('-='*30)
print('')
for ord in sorted(lista):
    print(ord)
print('')
print('-='*30)
print('')
print(f'O Cruzeiro se encontra na {lista.index("Cruzeiro")} ° possição')
print('')
print('-='*30)

#OU

lista = ('Flamengo',
'Palmeiras SP',
'Botafogo FR RJ',
'Bahia',
'CA Paranaense PR',
'São Paulo FC SP',
'Cruzeiro',
'Fortaleza CE',
'Red Bull Bragantino SP',
'Internacional RS',
'Atletico Mineiro MG',
'EC Juventude RS',
'Criciúma',
'Cuiabá Esporte Clube MT',
'EC Vitória BA',
'Vasco Gama',
'AC Goianiense GO',
'Gremio',
'Corinthians SP',
'Fluminense RJ')
print('-='*15)
print(f'Lista de times do Brasileirão: {lista}')
print('-='*15)
print(f'Os 5 Primeiros são: {lista[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {lista[-4]}')
print('-='*15)
print(f'Timeis em ordem alfabética: {sorted(lista)}')
print('-='*15)
print(f'O Cruzeiro está na {lista.index("Cruzeiro")+1}° posição')

