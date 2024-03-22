''' Crie um Script em Python que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. '''

print('Bem ao Fefelocar')
d = float(input('Quantos dias você ficou com carro?: '))
k = float(input('Quantos KM você rodou com o Carro?: '))
diaria = 60
km = 0.15
dd = diaria * d
kkm = k * km
t = dd + kkm
print('O valor total do aluguel ficou R${:.2f}, Você gastou R${:.2f} em KM e R${:.2f} em Diaria'.format(t, kkm, dd))
