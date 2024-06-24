INF = int(1e9)

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c :
        graph[a][b] = c
        # 기존의 코드는 한 경로에 대한 값이 여러 번 들어오면 무조건 마지막에 들어온 값으로 저장됐었음
        # 이 부분을 해결하기 위해 저장된 값과 비교하는 작업 추가
        # 그래프를 모두 무한대로 초기화 시켜놓았기 때문에 처음 들어오는 경로값이어도 정상 실행됨

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()