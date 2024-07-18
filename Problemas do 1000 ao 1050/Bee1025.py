caso = 1

while True:
    try:
        N, Q = map(int, input().strip().split())
        if N == 0 and Q == 0:
            break
        marmores = [0] * 10001 
        for _ in range(N):
            marmores[int(input())] += 1
        for i in range(1, 10001):
            marmores[i] += marmores[i - 1]
        print(f'CASE# {caso}:')
        caso += 1
        for _ in range(Q):
            x = int(input())
            if marmores[x] == marmores[x - 1]:
                print(f'{x} not found')
            else:
                print(f'{x} found at {marmores[x - 1] + 1}')
    except EOFError:
        break
