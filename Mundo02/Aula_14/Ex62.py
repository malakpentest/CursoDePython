'''Crie um Script em Python perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('GERADOR DE PA')
print('-='*10)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
print('-='*10)
t = 0
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(t), end='')
        t += razao
        cont += 1
    print('PAUSA')
    print('Quer sair digite 0')
    mais = int(input('Quantos termo você quer mostrar a mais?: '))
print('Progressão finalizada com {} termos mostrados'.format(total))
