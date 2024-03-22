''' Crie umScript em Python que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

s = float(input('Qual e o valor do seu salario R$:'))
maior = (s/100)*10+s
menor = (s/100)*15+s
if s<=1250.00:
    print('Seu almento e de 15% e vai ficar R$:{:.2f}'.format(menor))
else:
    print('Seu almento e de 10% e vai ficar R$:{:.2f}'.format(maior))

# Ou

s = float(input('Qual e o valor do funcionario? R$:'))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s *10 / 100)
print('Quem ganha R$:{:.2f} passa a ganhar R$:{:.2f} agora.'.format(s, n))
