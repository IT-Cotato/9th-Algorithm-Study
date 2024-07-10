import sys

n, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [i for i in range(d+1)]

for i in range(d+1):

    distance[i] = min(distance[i], distance[i-1]+1)

    for s, e, shortcut in graph:
        if i == s and e <= d and distance[i]+shortcut < distance[e]:
            distance[e] = distance[i]+shortcut

print(distance[d])