# Crie um Script em Python que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(2, 51, 2):
     print(c, end=' ')
print('Acabou!!')

# OU

for c in range(0 , 51):
    if c % 2 == 0:
        print(c , end=' ')
print('Acabou!!')
