''' Crie um Script em Python  que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO '''

print('Bem vindo!! a central de aluno')d
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
n3 = float(input('Digite sua nota: '))
n4 = float(input('Digite sua nota: '))
n5 = float(input('Digite sua nota: '))
resultado = (n1+n2+n3+n4+n5) / 5
if 7 > resultado >= 5:
    print('Sua nota e {:.1f} voce esta de recuperação'.format(resultado))
elif resultado <= 5.0:
    print('Sua nota e {:.1f} você foi reprovado precisa estudar mais !!!'.format(resultado))
elif resultado >= 6.9:
    print('Sua nota e {:.1f}, Meus PARABENS!! você foi APROVADO'.format(resultado))

# OU

print('Bem vindo!! a central de aluno')
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
n3 = float(input('Digite sua nota: '))
n4 = float(input('Digite sua nota: '))
n5 = float(input('Digite sua nota: '))
resultado = (n1+n2+n3+n4+n5) / 5
if 7 > resultado >= 5:
    print('Sua nota e {:.1f} voce esta de recuperação'.format(resultado))
elif resultado <= 5.0:
    print('Sua nota e {:.1f} você foi reprovado precisa estudar mais !!!'.format(resultado))
else:
    print('Sua nota e {:.1f}, Meus PARABENS!! você foi APROVADO'.format(resultado))
