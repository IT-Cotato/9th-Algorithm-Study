import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 그래프를 표현하기 위한 2차원 리스트 + 모든 값을 무한으로 초기화

# 시작 도시와 도착 도시가 같은 경우 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split()) # 시작 도시 a, 도착 도시 b, 비용 c
    # 도시와 도시를 연결하는 간선이 여러개 존재하는 경우
    # 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF: # 도달할 수 없는 경우
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()