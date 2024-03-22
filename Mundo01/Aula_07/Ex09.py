# Cria um Script que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('Ola, vou converter o valor em centimetros e milimitros ')
n1=int(input('digite o valor em METROS: '))
c= n1*100
m= n1*1000
print('O valor do metro que vc digitou e de {}, convertido em centimetros {:4}, e o mesmo em milimitros{:6}'.format(n1, c, m))
desafio 9
print('Ola, quer saber a tabuada de algum numero? consigo de mostrar ela ate o numero 10')
n1=int(input('Digite aqui o numero desejado: '))
s2=n1*2
s3=n1*3
s4=n1*4
s5=n1*5
s6=n1*6
s7=n1*7
s8=n1*8
s9=n1*9
s10=n1*10
print('A tabuada do numero {} e: \n'
      '{} x 1 ={}\n'
      '{} x 2 ={}\n'
      '{} x 3 ={}\n'
      '{} x 4 ={}\n'
      '{} x 5 ={}\n'
      '{} x 6 ={}\n'
      '{} x 7 ={}\n'
      '{} x 8 ={}\n'
      '{} x 9 ={}\n'
      '{} x 10 ={}\n'
      .format(n1, n1, n1, n1, s2 , n1, s3 , n1, s4 , n1, s5, n1, s6, n1, s7, n1, s8, n1, s9, n1, s10 ))
