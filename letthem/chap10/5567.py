import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 동기의 수 (상근이 포함)
m = int(input()) # 친구 관계의 수
graph = [[] for _ in range(n + 1)] # 친구 관계를 저장할 인접 리스트
visited = [0 for _ in range(n + 1)] # 방문 여부 및 각 노드까지의 거리를 저장할 리스트

# 친구 관계 입력 받기
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(x):
  q = deque()
  visited[x] = 1 # 시작 노드 방문 표시 (1로 초기화하여 방문 표시와 거리 계산)
  q.append(x)
  while q:
    a = q.popleft()
    for i in graph[a]:
      if visited[i] == 0: # 방문한 적이 없으면
        q.append(i) # 큐에 삽입
        visited[i] = visited[a] + 1 # 현재 노드까지의 거리 저장

bfs(1) # 상근이 1번 노드. 시작

# '상근이의 친구'와 '상근이 친구의 친구' 수 계산
result = 0
for i in range(2, n + 1):
  # 본인이거나 친구거나, 친구의 친구거나 경우의 수가 최대 3개
  if visited[i] < 4 and visited[i] != 0: # 거리가 3 이하여야 함
    result += 1

print(result)