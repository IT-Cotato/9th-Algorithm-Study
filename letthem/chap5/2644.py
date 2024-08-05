import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수 계산해야 하는 사람 a와 b
m = int(input()) # 부모 자식 관계의 개수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) # 방문처리 모두 false로 초기화
result = []
####

# 부모 자식 관계의 수만큼 돌면서
for _ in range(m):
  x, y = map(int, input().split()) # 부모 자식 관계인 노드들 graph에 저장
  graph[x].append(y)
  graph[y].append(x)

# dfs
def dfs(v, num):
  num += 1 # 현재 노드 방문 시 촌수 증가
  visited[v] = True # 현재 노드 방문 처리

  if v == b: # a와 계산할 목표 노드 b에 도착했으면
    result.append(num) # result에 num 넣기

  for i in graph[v]: # 해당 노드와 연결된(부모 자식 관계) 노드 탐색
    if not visited[i]: # 방문한 적 없으면
      dfs(i, num) # dfs 재귀

dfs(a, 0) # a (시작 노드), num(촌수)은 0인 상태로 dfs 시작

if len(result) == 0: # result가 없으면 -1
  print(-1)
else: # result가 있으면 result값에서 촌수를 1 빼서 출력 (dfs에서 바로 촌수 증가했기 때문에 -1해줘야 함)
  print(result[0] - 1)