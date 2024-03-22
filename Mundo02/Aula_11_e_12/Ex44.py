''' Crie um Script em Python que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros '''

print('Bem Vindo ao \n{:=^40}'.format('LOJAS FEFE SHOP'))
valor = float(input('Digite o valor do Seu produto R$ :'))
fp = int(input('''FORMA DE PAGAMENTO
[ 1 ] á Vista dinheiro/ Cheque
[ 2 ] á vista cartao
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual e a sua opção? :'''))
avista = valor-(valor/100*10)
avistaC = valor-(valor/100*5)
t = valor+(valor/100*20)

if fp == 1:
      print('Você tem 10% de desconto e sua compra ficou R$:{:.2f} de R$:{:.2f}'.format(avista, valor))
elif fp == 2:
      print('Você tem 5% de desconto e sua compra ficou R$:{:.2f} de R$:{:.2f}'.format(avistaC, valor))
elif fp == 3:
      print('Você nao tem desconto a sua compra ficou sem juros 2xR$:{} total a pagar R$:{:.2f}.'.format(valor/2, valor))
elif fp == 4:
      vezes = float(input('quantas vezes você pretende pagar? maximo 12x: '))
      print('Voce tem um acrescimo de 20% juros sua compra ficou em {:.0f}x de R$:{:.2f} o produto era R$:{:.2f} com juros do cartão ficou totalizando R$:{:.2f}.'.format(vezes, t/vezes , valor, t))
else:
      print('opção invalida')
