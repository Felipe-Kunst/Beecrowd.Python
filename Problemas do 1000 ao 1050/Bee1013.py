Valor1,Valor2,Valor3 = map(int,input().split())

maiorx = (Valor1 + Valor2 + abs(Valor1-Valor2))/2
maiorz = (maiorx + Valor3 + abs(maiorx-Valor3))/2
print(f'{maiorz:.0f} eh o maior')
