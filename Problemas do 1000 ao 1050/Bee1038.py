codigo,quantidade = map(int,input().split())
Total = float()
if(codigo == 1):
    Total = (4* quantidade)
elif(codigo == 2):
    Total = (4.5* quantidade)
elif(codigo == 3):
    Total = (5* quantidade)
elif(codigo == 4):
    Total = (2* quantidade)
elif(codigo == 5):
    Total = (1.5*quantidade)
print (f'Total: R$ {Total:.2f}')