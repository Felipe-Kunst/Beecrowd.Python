vitoriasdoInter = 0
vitoriasdoGremio = 0
empates = 0
TotaldeGols_Inter = 0
TotaldeGols_Gremio = 0
totaldeGrenais = 0

while True:
    GolsdoInter, GolsdoGremio = map(int, input().split())
    
    TotaldeGols_Inter += GolsdoInter
    TotaldeGols_Gremio += GolsdoGremio
    
    totaldeGrenais += 1
    
    if GolsdoInter > GolsdoGremio:
        vitoriasdoInter += 1
    elif GolsdoGremio > GolsdoInter:
        vitoriasdoGremio += 1
    else:
        empates += 1
    
    while True:
        print("Novo grenal (1-sim 2-nao)")
        novoGrenal = int(input())
        
        if novoGrenal in [1, 2]:
            break
    
    if novoGrenal == 2:
        break

print(f"{totaldeGrenais} grenais")
print(f"Inter:{vitoriasdoInter}")
print(f"Gremio:{vitoriasdoGremio}")
print(f"Empates:{empates}")

if vitoriasdoInter > vitoriasdoGremio:
    print("Inter venceu mais")
elif vitoriasdoGremio > vitoriasdoInter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
