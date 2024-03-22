# Crie um script Python que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
Crie um script Python Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n1=int(input('Digita um numero : '))
n2=int(input('Outro Numero : '))
s=n1+n2
print('A soma dos dois numero são {} , que fica antes do {}, e depois do {}.'.format(s, s-1, s+1))
