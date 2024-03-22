''' Crie um Script em Python que desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– abaixo de 18,5: MAGRESA
– 18,5 e 25: NORMAL
– 25 até 30: SOBREPESO
– 30 até 34.9: OBSIDADE °1
- 40 até 39.9: OBSIDADE °2
– Acima de 40: OBSIDADE °3 '''

print('Bem vindo ao cálculo de IMC')
p = float(input('Digite seu peso atual KG: '))
a = float(input('Digite sua altura atual M: '))
imc = p/(a**2)
if imc <18.5:
      print('Você esta com {:.1f}, abaixo do peso considerado MAGRESA'.format(imc))
elif 18.5 <= imc <=24.9:
      print('Você esta com {:.1f}, e você esta no peso NORMAL'.format(imc))
elif 25 <= imc < 29.9:
      print('Você esta com {:.1f}, acima do peso consideravel com SOBREPESO'.format(imc))
elif 30 <= imc <34.9:
      print('Você está com {:.1f}, acima do peso consideravel com OBESIDADE °1'.format(imc))
elif 35 <= imc <39.9:
      print('Você está com {:.1f}, acima do peso consideravel com OBSIDADE °2'.format(imc))
elif 40 <= imc:
      print('Você está com {:.1f}, acima do peso consideravel com OBSIDADE °3'.format(imc))
