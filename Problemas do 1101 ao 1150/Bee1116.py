Casos = int(input())
for i in range(Casos):
    X,Y=list(map(int,input().split()))
    if(Y == 0):
        print("divisao impossivel")
    else:
        print(f"{(X / Y):0.1f}")