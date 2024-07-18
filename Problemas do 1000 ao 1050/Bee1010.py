Peca1,Quantidade1,Valor1= (input().split(' '))
Peca2,Quantidade2,Valor2= (input().split(' '))
Quantidade1=int(Quantidade1)
Quantidade2=int(Quantidade2)
Valor1=float(Valor1)
Valor2=float(Valor2)
Apagar=Valor1*Quantidade1+Valor2*Quantidade2
print(f'VALOR A PAGAR: R$ {Apagar:.2f}')