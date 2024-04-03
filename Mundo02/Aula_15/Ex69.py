''''Crie um Script em Python que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''


idade = sexo = cont = masculino = feminino =  0
while True:
    print('=-'*30)
    print(f'{"CADASTRO DE PESSOAS":^60}')
    print('=-'*30)
    idade =int(input('Digite sua idade: '))
    print(f'''{'Qual e o seu sexo':^30}\n
    {'[M] - Masculino':^15}
    {'[F] - Feminino':^15} ''')
    sexo = str(input('[ M/F ]: ')).upper().strip()[0]
    print('=-'*30)
    if sexo == 'M':
        masculino += 1
        if idade > 18:
            cont += 1
    if sexo == 'F':
        if  idade < 18:
            feminino += 1
    continuar = str(input('Você deseja continuar [S/N] : ')).upper().strip()[0]
    if continuar == 'N':
        print('Obrigado volte sempre!!!')
        break
print(f'Tem {masculino} homens ao total e tem {cont} homens maior de 18 anos e {feminino} munlher com menor de 20 anos ')

# OU


tot18 = toth = totm20 =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth +=1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Tota; de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')
