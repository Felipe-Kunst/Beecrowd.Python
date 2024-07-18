Valor=int(input())
print(Valor)

Notade100 = Valor // 100
Valor = Valor - Notade100*100
Notade50 = Valor // 50
Valor = Valor - Notade50*50
Notade20 = Valor // 20
Valor = Valor - Notade20*20
Notade10 = Valor // 10
Valor = Valor - Notade10*10
Notade5 = Valor // 5
Valor = Valor - Notade5*5
Notade2 = Valor // 2
Valor = Valor - Notade2*2
Moedade1real = Valor // 1
Valor = Valor - Moedade1real*1

print('{} nota(s) de R$ 100,00'.format(Notade100))
print('{} nota(s) de R$ 50,00'.format(Notade50))
print('{} nota(s) de R$ 20,00'.format(Notade20))
print('{} nota(s) de R$ 10,00'.format(Notade10))
print('{} nota(s) de R$ 5,00'.format(Notade5))
print('{} nota(s) de R$ 2,00'.format(Notade2))
print('{} nota(s) de R$ 1,00'.format(Moedade1real))