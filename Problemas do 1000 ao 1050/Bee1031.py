def restante(n, k, i, r):
    if i >= n:
        return r
    return restante(n, k, i + 1, (r + k) % i)

def encontrar_y(n, y):
    if restante(n, y, 1, 0) != 11:
        return encontrar_y(n, y + 1)
    return y

n = int(input())
while n != 0:
    y = encontrar_y(n, 1)
    print(y)
    n = int(input())
