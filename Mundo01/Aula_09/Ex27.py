# Crie um Script em Python que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Prazer {} seu primeiro nome e {} e o seu ultimo nome e {}'.format(nome, n[0], n[len(n)-1]))

# OU

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer')
print('Seu nome e {}'.format(nome))
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
