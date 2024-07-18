VetorPrincipal= []
VetorAux = []

for i in range(20):
    valor = int(input())
    VetorPrincipal.append(valor)
    
Indice = 19 
   
for i in range(20):
    VetorAux.append(VetorPrincipal[i])
    if i >=10:
        VetorPrincipal[i] = VetorAux[Indice]
    else:
        VetorPrincipal[i] = VetorPrincipal[Indice]        
    Indice-=1

for i in range(20):
    print('N[{0}] = {1}'.format(i,VetorPrincipal[i]))
