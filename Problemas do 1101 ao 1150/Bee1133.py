X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

while X <= Y:
    if X % 5 == 2 or X % 5 == 3:
        print(X)
    X += 1
