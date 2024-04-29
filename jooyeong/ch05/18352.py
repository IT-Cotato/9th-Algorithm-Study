# BFS로 풂
from collections import deque

n, m, k, x = map(int, input().split())
# n 도시의 개수, m 도로의 개수, k 거리 정보, x 출발 도시의 번호
graph = [[] for i in range(n+1)] # 그래프 생성

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 그래프에 a 도시에서 b 도시로 가는 길이 있음을 추가

distance = [-1] * (n+1) # 그래프상 노드 간의 거리 초기화
distance[x] = 0
q = deque([x])

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now]+1
            q.append(next)
            # 지나간 적 없는 도시면 해당 도시 방문

if k not in distance:
    print(-1)
    # 거리가 k에 해당하는 도시가 없을 경우 -1 출력
else:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)