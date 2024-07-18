import math
A,B,C = map(float,input().split())
Baskara = (B**2)-(4*A*C)
if(Baskara <0 or A==0):
    print("Impossivel calcular")
else:
    Baskara=math.sqrt(Baskara)
    R1 = (-B+Baskara)/(2*A)
    R2 = (-B-Baskara)/(2*A)
    print(f'R1 = {R1:0.5f}')
    print(f'R2 = {R2:0.5f}')