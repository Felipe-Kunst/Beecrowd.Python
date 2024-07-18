Vetor = []
for i in range(100):
    Valor = float(input())
    Vetor.append(Valor)
    if Valor <= 10.0:
        print('A[{}] = {}'.format(i,Valor))