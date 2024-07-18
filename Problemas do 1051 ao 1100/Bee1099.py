Casos = int(input())
for i in range(Casos):
    Valor1,Valor2 = list(map(int, input().split()))
    Impares = 0
    if(Valor1==Valor2):
        print(0)
    else:
        Par = 0
        if (Valor1 > Valor2):
            Par = Valor1
            Valor1 = Valor2
            Valor2 = Par
        while (Valor1 < ( Valor2- 1)):
            Valor1 += 1
            if(Valor1 % 2 != 0):
                Impares+= Valor1
        print(Impares)