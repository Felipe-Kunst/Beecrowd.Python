def soma(Matriz, Coluna):
    Soma = 0
    for i in range(12):
        Soma += Matriz[i][Coluna]    
    return Soma

def Media(Matriz, Coluna):
    Media = 0
    for i in range(12):
        Media +=  Matriz[i][Coluna]
    return Media/12

ColunaDesejada = int(input())
Operadores= input()

Matiz = []

for i in range(12):
    linha = []
    for j in range (12):
        linha.append(float(input()))
    Matiz.append(linha)

if Operadores == 'S':
    Resultado = soma(Matiz, ColunaDesejada)
    print(f'{Resultado:.1f}')
elif Operadores == 'M':
    Resultado = Media(Matiz, ColunaDesejada)
    print(f'{Resultado:.1f}')