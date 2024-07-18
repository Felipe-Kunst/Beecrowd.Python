while(True):
    try:
        Valor1,Valor2=list(map(int,input().split()))
        if(Valor1==0 or Valor2==0):
                break
        elif(Valor1>0 and Valor2>0):
            print("primeiro")
        elif(Valor1>0 and Valor2<0):
            print("quarto")
        elif(Valor1<0 and Valor2<0):
            print("terceiro")
        elif(Valor1<0 and Valor2>0):
             print("segundo")
    except EOFError:
        break