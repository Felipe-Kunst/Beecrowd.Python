operacao = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)

if operacao == 'S':
    soma = 0
    Colunainicial = 1
    for i in range(0, 11):
        for j in range(Colunainicial, 12):
            soma += matriz[i][j]
        Colunainicial += 1
    print('{:.1f}'.format(soma))

if operacao == 'M':
    soma = 0
    Colunainicial = 1
    contador_elementos = 0
    for i in range(0, 11):
        for j in range(Colunainicial, 12):
            soma += matriz[i][j]
            contador_elementos += 1
        Colunainicial += 1
    media = soma / contador_elementos
    print('{:.1f}'.format(media))
