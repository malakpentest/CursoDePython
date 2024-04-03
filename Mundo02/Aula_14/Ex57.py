'''Crie um Script em Python que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente
até ter um valor correto'''

sexo = str(input('Informe seu [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(sexo))
