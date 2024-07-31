import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
v = int(input()) # 연결된 간선의 수
graph = [[] for i in range(n + 1)] # 각 컴퓨터에 연결되어 있는 컴퓨터에 대한 정보 담는 리스트 초기화
visited = [0] * (n + 1) # 방문 여부 - 모두 방문 안 한 걸로 초기화

# 그래프 생성
for i in range(v): 
  a, b = map(int,input().split())
  graph[a] += [b] # 그래프 a에 b 연결
  graph[b] += [a] # 그래프 b에도 a 연결

# dfs
def dfs(v): # 방문할 컴퓨터 번호 v 입력 받음
  visited[v] = 1 # 바로 방문 표시
  for next in graph[v]: # 그래프에 연결된 다음 노드 탐색
    if visited[next] == 0: # 다음 노드가 방문한 적 없다면
      dfs(next) # 재귀적으로 dfs

dfs(1) # 문제에서 1번 컴퓨터부터 dfs 시작
print(sum(visited) - 1) # 1번 컴퓨터 제외하고 1번 컴퓨터와 연결된 컴퓨터 개수 출력해야 하므로 '-1'
