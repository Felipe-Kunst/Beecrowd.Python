from math import gcd

def simplificar(numerador, denominador):
    divisor_comum = gcd(numerador, denominador)
    return numerador // divisor_comum, denominador // divisor_comum

N = int(input().strip())

for _ in range(N):
    linha = input().strip().split()
    N1, D1 = int(linha[0]), int(linha[2])
    N2, D2 = int(linha[4]), int(linha[6])
    operador = linha[3]

    if operador == '+':
        resultado_numerador = N1 * D2 + N2 * D1
        resultado_denominador = D1 * D2
    elif operador == '-':
        resultado_numerador = N1 * D2 - N2 * D1
        resultado_denominador = D1 * D2
    elif operador == '*':
        resultado_numerador = N1 * N2
        resultado_denominador = D1 * D2
    elif operador == '/':
        resultado_numerador = N1 * D2
        resultado_denominador = N2 * D1

    resultado_simplificado = simplificar(resultado_numerador, resultado_denominador)

    print(f"{resultado_numerador}/{resultado_denominador} = {resultado_simplificado[0]}/{resultado_simplificado[1]}")
