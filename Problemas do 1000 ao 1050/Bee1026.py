import sys

def somador_mofiz(a, b):
    return a ^ b  

for line in sys.stdin:
    a, b = map(int, line.split())
    resultado = somador_mofiz(a, b)
    print(resultado)
