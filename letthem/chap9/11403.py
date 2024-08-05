n = int(input()) # n개의 줄
graph = [list(map(int, input().split())) for _ in range(n)] # 그래프의 인접 행렬. 1 - 간선 O, 0 - 간선 X
    
#플로이드-워셜 알고리즘
for k in range(n): #경로 for문이 가장 상위 단계여야 누락되지 않는다
  for i in range(n):
    for j in range(n): 
      if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1): # 직접 연결되어 있거나 다른 노드를 거쳐 가는 길이 있거나
        graph[i][j] = 1

for g in graph:
  print(*g)