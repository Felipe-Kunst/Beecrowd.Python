Valor = float(input())

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

Moedade1real=float('%.2f'% Moedade1real)
Valor=float('%.2f'% Valor)

Moedade50centavos = Valor // 0.5
Valor = Valor - Moedade50centavos*0.5
Moedade50centavos=float('%.2f'% Moedade50centavos)
Valor=float('%.2f'% Valor)

Moedade25centavos = Valor // 0.25
Valor = Valor - Moedade50centavos*0.25
Moedade50centavos=float('%.2f'% Moedade50centavos)
Valor=float('%.2f'% Valor)

Moedade10centavos = Valor // 0.10
Valor = Valor - Moedade10centavos*0.10
Moedade10centavos=float('%.2f'% Moedade10centavos)
Valor=float('%.2f'% Valor)

Moedade5centavos = Valor // 0.05
Valor = Valor - Moedade5centavos*0.05
Moedade5centavos=float('%.2f'% Moedade5centavos)
Valor=float('%.2f'% Valor)

Moedade1centavos = Valor * 100
Moedade5centavos=float('%.2f'% Moedade5centavos)
Valor=float('%.2f'% Valor)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(Notade100)))
print('{} nota(s) de R$ 50.00'.format(int(Notade50)))
print('{} nota(s) de R$ 20.00'.format(int(Notade20)))
print('{} nota(s) de R$ 10.00'.format(int(Notade10)))
print('{} nota(s) de R$ 5.00'.format(int(Notade5)))
print('{} nota(s) de R$ 2.00'.format(int(Notade2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(Moedade1real)))
print('{} moeda(s) de R$ 0.50'.format(int(Moedade50centavos)))
print('{} moeda(s) de R$ 0.25'.format(int(Moedade25centavos)))
print('{} moeda(s) de R$ 0.10'.format(int(Moedade10centavos)))
print('{} moeda(s) de R$ 0.05'.format(int(Moedade5centavos)))
print('{} moeda(s) de R$ 0.01'.format(int(Moedade1centavos)))