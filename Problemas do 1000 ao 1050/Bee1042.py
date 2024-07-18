Numero1,Numero2,Numero3 = map(int,input().split())

if ( Numero2 < Numero1 ) and ( Numero1 > Numero3 ):
    if (Numero2 > Numero3):
        print (f'{Numero3}\n{Numero2}\n{Numero1}') 
        print(f'\n{Numero1}\n{Numero2}\n{Numero3}')
    elif (Numero3 > Numero2):
        print (f'{Numero2}\n{Numero3}\n{Numero1}') 
        print(f'\n{Numero1}\n{Numero2}\n{Numero3}')
if ( Numero1 < Numero2 ) and ( Numero2 > Numero3 ):
        if (Numero1 > Numero3):
            print (f'{Numero3}\n{Numero1}\n{Numero2}') 
            print(f'\n{Numero1}\n{Numero2}\n{Numero3}')
        elif (Numero3 > Numero1):
            print (f'{Numero1}\n{Numero3}\n{Numero2}') 
            print(f'\n{Numero1}\n{Numero2}\n{Numero3}')

if ( Numero2 < Numero3 ) and ( Numero3 > Numero1 ):
        if (Numero1 > Numero2):
            print (f'{Numero2}\n{Numero1}\n{Numero3}') 
            print(f'\n{Numero1}\n{Numero2}\n{Numero3}')
        elif (Numero2 > Numero1):
            print (f'{Numero1}\n{Numero2}\n{Numero3}')
            print(f'\n{Numero1}\n{Numero2}\n{Numero3}')