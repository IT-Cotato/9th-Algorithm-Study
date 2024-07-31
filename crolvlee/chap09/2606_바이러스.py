# 1번 컴퓨터를 출발 노드로 설정

# 특정 컴퓨터와 연결되어 있는 컴퓨터에 방문하지 않았다면 그 컴퓨터의 번호를 매개변수로 전달하면서 재귀호출
# 함수가 호출되는 수 == 감염된 컴퓨터의 수



N = int(input())  # 컴퓨터의 개수
M = int(input())  # 연결된 컴퓨터 쌍의 개수

def dfs(graph, v, visited):
  global cnt
  visited[v] = True   # 방문했으니 True로 바꿔줌
  for i in graph[v]:
    if visited[i] == False:
      cnt += 1
      dfs(graph, i, visited)

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0   # 함수가 호출되는 수 (감염된 컴퓨터의 수)

# 그래프에 연결된 컴퓨터들 채워넣기
for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(graph, 1, visited)
print(cnt)