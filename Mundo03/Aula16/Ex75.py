
a = int(input('Digite um Número: '))
b = int(input('Digite outro Número: '))
c = int(input('Digite mais um Número: '))
d = int(input('Digite o último Número: '))
e = 0
lista = (a,b,c,d)
print(f'você digitou esses número {lista}')
while True:
    if a == 9:
        e = e + 1
        if b == 9:
            e = e + 1
            if c == 9:
                e = e + 1
                if d == 9:
                    e = e + 1
                    break
    if b == 9:
        e = e + 1
        if c == 9:
            e = e + 1
            if d == 9:
                e = e + 1
                break
    if c == 9:
        e = e + 1
        if d == 9:
            e = e + 1
            break
    if d == 9:
        e = e + 1
        break
    else:
        print('o numero 9 nào foi digitada nenhuma vez')
        break
    print('o numero 9 foi digitada {} vezes'.format(e))
while enumerate(lista):
    if a == 3:
        print('o numero 3 foi digitado na posição 1')
        break
    if b == 3:
        print('o numero 3 foi digitado na posição 2')
        break
    if c == 3:
        print('o numero 3 foi digitado na posição 3')
        break
    if d == 3:
        print('o numero 3 foi digitado na posição 4')
        break
    else:
        print('O número 3 nao foi digitado')
        break
a1 = a % 2
b1 = b % 2
c1 = c % 2
d1 = d % 2
while True:
    if a1 == 0:
        a1 = a
        if b1 == 0:
            b1 = b
            if c1 == 0:
                c1 = c
                if d1 == 0:
                    d1 = d
                    print('esse numeros sao pares {} {} {} {}'.format(a, b, c, d))
                    break
    elif b1 == 0:
        b1 = b
        if c1 == 0:
            c1 = c
            if d1 == 0:
                d1 = d
                print('esse numeros sao pares {} {} {}'.format(b,c,d))
                break
    elif c1 == 0:
        c1 = c
        if d1 == 0:
            d1 = d
            print('esse numeros sao pares {} {}'.format(c,d))
            break
    elif d1 == 0:
        d1 = d
        print('esse numero e par {}'.format(d))
        break

#OU

núm = (int(input('Digite um numero:')),int(input('Digite outro numero:')),int(input('Digite mais um numero:')),int(input('Digite o último numero:')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('Ovalor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ',end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
