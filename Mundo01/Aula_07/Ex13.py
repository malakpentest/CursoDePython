# Crie um Script em Python que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('Bem vindo, Funcionario')
n1=float(input('Digite o valor do seu salario :'))
s=n1/100
t=s*115
print('O valor do seu salario e de R${:.2f}, com novo almento ele ficara : R${:.2f}'.format(n1, t))
