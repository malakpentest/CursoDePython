
listagem = ('Caneta',1.90,'Lápis',1.00,'Borracha',0.50,'Apontador', 0.90,'Caderno',4.90,'Agenda',19.90,'Revista',15.49,'Compasso',3.99,'Estojo',4.99,'Mochila',149.90,'Regua', 6.90 )
print('=='*30)
print('{:^60}'.format('TABELA DE PREÇOS'))
print('=='*30)
print('{}{}R$    {:.2f}'.format(listagem[0],'.'*44,listagem[1]))
print('{}{}R$    {:.2f}'.format(listagem[2],'.'*45,listagem[3]))
print('{}{}R$    {:.2f}'.format(listagem[4],'.'*42,listagem[5]))
print('{}{}R$    {:.2f}'.format(listagem[6],'.'*41,listagem[7]))
print('{}{}R$    {:.2f}'.format(listagem[8],'.'*43,listagem[9]))
print('{}{}R$   {:.2f}'.format(listagem[10],'.'*44,listagem[11]))
print('{}{}R$   {:.2f}'.format(listagem[12],'.'*43,listagem[13]))
print('{}{}R$    {:.2f}'.format(listagem[14],'.'*42,listagem[15]))
print('{}{}R$    {:.2f}'.format(listagem[16],'.'*44,listagem[17]))
print('{}{}R$  {:.2f}'.format(listagem[18],'.'*43,listagem[19]))
print('{}{}R$    {:.2f}'.format(listagem[20],'.'*45,listagem[21]))
print('=='*30)

#OU

listagem = ('Caneta',1.90,'Lápis',1.00,'Borracha',0.50,'Apontador', 0.90,'Caderno',4.90,'Agenda',19.90,'Revista',15.49,'Compasso',3.99,'Estojo',4.99,'Mochila',149.90,'Regua', 6.90 )
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
