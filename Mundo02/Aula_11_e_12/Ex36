''' Crie um Script em Python para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

from time import sleep

str(print('-=-=-=-###=-=--'*3))
str(print('Bem Vindo Ao Cadastro para Comprar a sua Casa!'))
str(print('-=-=-=-###=-=--'*3))
salario = float(input('valor do seu salario: '))
casa = float(input('valor da casa: '))
anos = int(input('quantos anos vc pretende pagar: '))
meses = anos*12
emprestimo = casa / meses
s1 = salario/100*30
if emprestimo <= s1:
    print('Parabéns Seu imprestimo esta aprovado!!')
    print('Seu imprestimo vai ficar em {}x de {:.2f} '.format(meses, emprestimo))
elif emprestimo >= s1:
    print('Infelismente vc nao foi aprovado')
