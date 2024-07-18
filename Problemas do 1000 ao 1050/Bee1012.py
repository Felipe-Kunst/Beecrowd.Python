A,B,C=(input().split(' '))
A=float(A)
B=float(B)
C=float(C)
Triangulo= A*C/2
Circulo= 3.14159*C**2
trapezio=(A+B)*C/2
Quadrado= B**2
retangulo=A*B
print(f'TRIANGULO: {Triangulo:.3f}')
print(f'CIRCULO: {Circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {Quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')