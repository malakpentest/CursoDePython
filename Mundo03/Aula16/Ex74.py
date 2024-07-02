#Desafio 74
import random
a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
d = random.randint(0,10)
e = random.randint(0,10)
lista=(a,b,c,d,e)
print('Os valores sorteado:')
print(lista)
while True:
    if a > b:
        if a > c:
            if a > d:
                if a > e:
                 print(f'o maior valor sorteado foi {a}')
                 break
    if b > a:
        if b > c:
            if b > d:
                if b > e:
                    print(f'o maior valor sorteado foi {b}')
                    break
    if c > a:
        if c > b:
            if c > d:
                if c > e:
                    print(f'o maior valor sorteado foi {c}')
                    break
    if d > a:
        if d > b:
            if d > c:
                if d > e:
                    print(f'o maior valor sorteado foi {d}')
                    break
    if e > a:
        if e > b:
            if e > c:
                if e > d:
                    print(f'o maior valor sorteado foi {e}')
                    break
while True:
    if a < b:
        if a < c:
            if a < d:
                if a < e:
                    print(f'o menor valor sorteado foi {a}')
                    break
    if b < a:
        if b < c:
            if b < d:
                if b < e:
                    print(f'o menor valor sorteado foi {b}')
                    break
    if c < a:
        if c < b:
            if c < d:
                if c < e:
                    print(f'o menor valor sorteado foi {c}')
                    break
    if d < a:
        if d < b:
            if d < c:
                if d < e:
                    print(f'o menor valor sorteado foi {d}')
                    break
    if e < a:
        if e < b:
            if e < c:
                if e < d:
                     print(f'o menor valor sorteado foi {e}')
                     break
#Ou

from random import randint
numeros = (randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10))
print('Os valores sorteados')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
