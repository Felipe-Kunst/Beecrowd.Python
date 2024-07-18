T = 0

while True:
    N = int(input())
    if N == 0:
        break
    
    if T > 0:
        print()

    totalX = 0
    totalY = 0
    consumos = [0] * 201
    
    for _ in range(N):
        X, Y = map(int, input().split())
        totalX += X
        totalY += Y
        consumos[Y // X] += X

    T += 1
    print(f"Cidade# {T}:")

    results = [f"{consumos[i]}-{i}" for i in range(201) if consumos[i] > 0]
    print(" ".join(results))
    
    consumo_medio = (totalY * 100) / totalX
    print(f"Consumo medio: {consumo_medio:.2f} m3.")
