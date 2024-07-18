valor = 0
countpar = 0
countImpar =0
countPosistivo=0
countNegativo=0

for i in range(5):
    valor=int(input())
    if valor%2 == 0:
        countpar += 1
    else:
        countImpar += 1
    if valor > 0:
        countPosistivo += 1
    elif valor <0:
        countNegativo +=1

print(f'{countpar} valor(es) par(es)')
print(f'{countImpar} valor(es) impar(es)')
print(f'{countPosistivo} valor(es) positivo(s)')
print(f'{countNegativo} valor(es) negativo(s)')