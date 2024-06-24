INF = int(1e9) # 무한을 의미

n = int(input()) # 도시의 개수 (노드)
m = int(input()) # 버스의 개수 (간선)

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원 리스트로 만들고 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 버스(간선)에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # a에서 b로 가는 비용 c
  a, b, c = map(int, input().split())
  if c < graph[a][b]:
    graph[a][b] = c

# 점화식. 플로이드 워셜 알고리즘
for k in range(1, n + 1): # 노드 1부터 1을 k로 두고 거쳐가게끔 점화식. ex) 4->2 : 4->1 + 1->2
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할 수 없는 경우, 0 출력
    if graph[a][b] == INF:
      print(0, end=" ")
    # 도달할 수 있는 경우, 거리 출력
    else:
      print(graph[a][b], end=" ")
  print()