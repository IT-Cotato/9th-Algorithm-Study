import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        friend_num = queue.popleft()
        for people_num in graph[friend_num]:
            queue.append(people_num)
            visited[people_num] = visited[friend_num] + 1

bfs(1)
result = 0
for i in range(2, n+1):
    if 0 < visited[i] <= 3:
        result += 1
        
print(result)