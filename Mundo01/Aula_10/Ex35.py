''' Crie um Script em Python que leia o comprimento de três retas e diga ao 
usuário se elas podem ou não formar um triângulo.'''

r1 = float(input('digite um segmento: '))
r2 = float(input('digite um segmento: '))
r3 = float(input('digite um segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima pode Forma um Triângulo')
else:
    print('Os segmentos acima não Forma um Triângulo')
