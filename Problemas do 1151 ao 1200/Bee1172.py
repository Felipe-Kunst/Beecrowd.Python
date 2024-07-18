def imprime_vetor(vetor):
    for i in range(10):
        print(f'X[{i}] = {vetor[i]}')

vetor = []

for i in range(10):
    valor = int(input())  
    
    if valor <= 0:
        vetor.append(1)
    else:
        vetor.append(valor)  

imprime_vetor(vetor)
