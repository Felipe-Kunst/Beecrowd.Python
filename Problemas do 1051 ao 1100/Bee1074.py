Quantidade=int(input())
for i in range(Quantidade):
    Valor=int(input())
    if(Valor<0):
        if(Valor%2==0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif(Valor>0):
        if(Valor % 2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif(Valor==0):
        print("NULL")