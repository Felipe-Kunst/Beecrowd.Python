def josephus(n, k):
    resultado = 0  
    for i in range(1, n + 1):
        resultado = (resultado + k) % i 
    return resultado + 1  

NC = int(input())
for caso in range(1, NC + 1):
    n, k = map(int, input().split())
    sobrevivente = josephus(n, k)
    print(f"Case {caso}: {sobrevivente}")
