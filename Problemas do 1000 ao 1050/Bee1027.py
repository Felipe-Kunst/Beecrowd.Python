def max_pontos_criticos(pontos):
    from collections import defaultdict

    y_menos_1 = []
    y_mais_1 = []

    for x, y in pontos:
        if y == -1:
            y_menos_1.append(x)
        elif y == 1:
            y_mais_1.append(x)

    y_menos_1.sort()
    y_mais_1.sort()

    contagem_maxima = 0
    i, j = 0, 0
    ultimo_x = -float('inf')

    while i < len(y_menos_1) or j < len(y_mais_1):
        if contagem_maxima % 2 == 0 and i < len(y_menos_1):  # y = a - 1
            x_atual = y_menos_1[i]
            if x_atual > ultimo_x:
                contagem_maxima += 1
                ultimo_x = x_atual
            i += 1
        elif contagem_maxima % 2 == 1 and j < len(y_mais_1):  # y = a + 1
            x_atual = y_mais_1[j]
            if x_atual > ultimo_x:
                contagem_maxima += 1
                ultimo_x = x_atual
            j += 1

    return contagem_maxima

import sys

entrada = sys.stdin.read
dados = entrada().strip().split('\n')
indice = 0
resultado = []

while indice < len(dados):
    N = int(dados[indice])
    indice += 1
    pontos = []

    for _ in range(N):
        x, y = map(int, dados[indice].split())
        pontos.append((x, y))
        indice += 1

    resultado.append(max_pontos_criticos(pontos))

for res in resultado:
    print(res)
