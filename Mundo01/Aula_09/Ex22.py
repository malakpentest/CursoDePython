''' Crie um Script em Pytohn que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome =str(input('Digite seu Nome: ')).strip()
print('Analisando seu Nome...')
print('Seu nome em Minúsculo é: {}'.format(nome.lower()))
print('Seu nome em Maiúsculo é: {}'.format(nome.upper()))
print('Nome tem {} Letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa =nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

# OU

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome maiúsculo e {}'.format(nome.upper()))
print('Seu nome minúsculo e {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome {} tem {} letras no primeiro nome'.format(separa[0],len(separa[0])))

# Ou

nome = str(input('Digite o seu nome: ').strip())
print('Seu nome em maiúsculo fica assim {}'.format(nome.upper()))
print('Seu nome em minúsculo fica assim{}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
separa = (nome.split())
print('Seu nome e {} e tem {} letras no primeiro nome'.format(separa[0],len(separa[0])))
