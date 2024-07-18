A,B,C = map(float,input().split())

if (A+B)> C and (B+C) > A and (C+A) > B :
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:0.1f}")
else :
    area= 0.5 * (A+B) * C
    print(f"Area = {area:0.1f}")