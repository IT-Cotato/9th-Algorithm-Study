n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
INF = int(1e9)

# 그래프 초기화 (거리를 모두 INF로)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

# 플로이드 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0",  end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
