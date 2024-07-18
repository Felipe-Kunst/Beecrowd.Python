MAXSIZE = 3502
MAXPRIME = 32650

primos = []

def josephus(n):
    retorno = 0
    for i in range(1, n + 1):
        retorno = (retorno + primos[n - i]) % i
    return retorno + 1

def eh_primo(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def preenche_primos():
    for i in range(2, MAXPRIME):
        if eh_primo(i):
            primos.append(i)  
preenche_primos()

while True:
    n = int(input())
    if n == 0:
        break
    print(josephus(n))
