# Crie um Script em Python que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pn = int(input('Digite um numero: '))
sn = int(input('Digite o Segundo numero: '))
decimo = primeiro + (10 - 1) * sn
for c in range(pn , decimo + sn, sn):
    print('{} '.format(c), end='→ ')
print('ACABOU')
