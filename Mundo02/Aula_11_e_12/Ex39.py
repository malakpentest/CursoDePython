''' Crie um Script em Python que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
sexo = int(input('''Você e homem ou mulher?
[ 1 ] Homem
[ 2 ] Mulher
:'''))
if sexo == 1:
    atual = date.today().year
    (print('Bem Vindo ao Serviço de Alistamento'))
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('quem nasceu em {} tem anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('sua hora de alistamento e para o dia 20/03/2024')
    elif idade < 18:
        saldo = 18 - idade
        print('vc ainda nao pode você tem {} se alistar'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento sera em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('vc passou da idade de alistamento vc passou {} Anos, pague uma multa de R$:{:.2f}, e aguarde ate o proxima convocação'.format(saldo, (idade-18)*2))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
elif sexo == 2:
    print('Você nao precisa se alistar por que vc e mulher!')
else:
    print('alternativa errada')
