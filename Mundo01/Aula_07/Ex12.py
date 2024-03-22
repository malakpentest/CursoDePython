#Crie um script em Python que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Bem Vindo ao fefeshop \n Estamos hoje com uma super desconto de 5% para toda loja')
n1=float(input('Digite o valo do produto r$:'))
s=n1/100
t=s*95
print('O valor do produto era {}, com valor do produto com valor de 5% de desconto fica {} '.format(n1, t))
