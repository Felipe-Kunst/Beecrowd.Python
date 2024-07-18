fibonacci = [0, 1]
TermoAnterior = 0
TermoAtual = 1

for i in range(2, 61):  
    proximo_termo = TermoAtual + TermoAnterior
    fibonacci.append(proximo_termo)
    TermoAnterior = TermoAtual
    TermoAtual = proximo_termo

Casos = int(input()) 
for i in range(Casos):
    X = int(input()) 
    print('Fib(%d) = %d' % (X, fibonacci[X]))
