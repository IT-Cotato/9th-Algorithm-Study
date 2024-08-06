import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
graph = [[] for i in range(n+1)]
while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    queue = deque([])
    queue.append([s, 0])
    v = [False] * (n+1)
    v[s] = True
    score = -1
    while queue:
        cur_p, cur_score = queue.popleft()
        for f in graph[cur_p]:
            if v[f] == False:
                v[f] = True
                score = max(score, cur_score+1)
                queue.append([f, cur_score+1])
    for i in range(1,n+1):
        if not v[i]:
            return INF
    return score

cand = []
min = INF
for j in range(1, n+1):
    temp = bfs(j)
    if temp == INF:
        continue
    if temp < min:
        cand = []
        cand.append(j)
        min = temp
    elif temp == min:
        cand.append(j)

print(min, len(cand))
print(" ".join(list(map(str, sorted(cand)))))