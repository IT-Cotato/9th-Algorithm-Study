from sys import stdin
input = stdin.readline
from collections import deque

def bfs():
    check = [-1] * 100001
    check[N] = 0
    Q = deque([N])
    time = 0
    while time == 0:
        qlen = len(Q)
        for _ in range(qlen):
            x = Q.popleft()
            if x == K:
                time += 1
            for nx in (x-1, x+1, x*2):
                if not (0 <= nx < 100001):
                    continue
                if check[nx] == -1 or check[nx] == check[x]+1:
                    check[nx] = check[x] + 1
                    Q.append(nx)

    print(check[K])
    print(time)

N, K = map(int, input().split())
if N >= K:
    print(N-K)
    print(1)
else:
    bfs()