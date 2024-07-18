X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

NaoMutiplosde13 = 0

for Num in range(X, Y + 1):
    if Num % 13 != 0:
        NaoMutiplosde13 += Num

# Impressão do resultado
print(NaoMutiplosde13)
