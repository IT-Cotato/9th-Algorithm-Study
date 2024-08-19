from collections import deque
 
n = int(input()) # 지도 n * n
graph = []
maxNum = 0 # 지도 최대 높이 값 0으로 초기화
 
for i in range(n):
  graph.append(list(map(int, input().split()))) # 지도 데이터 삽입
  for j in range(n):
    if graph[i][j] > maxNum:
      maxNum = graph[i][j] # 지도 최대 높이 값 넣어놓기

# 상하좌우 설정 
dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]

def bfs(a, b, value, visited):
  q = deque()
  q.append((a, b)) # a, b에서 시작하여 주변 이동하면서 현재 물 높이(value)보다 높은 지점 탐색
  visited[a][b] = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n: # 범위 내에서
        if graph[nx][ny] > value and visited[nx][ny] == 0: # 현재 물 높이보다 크고 방문한 적 없으면
          visited[nx][ny] = 1 # 방문 처리 -> 다신 방문 못하게 함
          q.append((nx, ny)) # q에 삽입
 
 
result = 0 # 최대 안전 영역의 개수 저장

for i in range(maxNum): # 물의 높이를 0부터 maxNum - 1까지 변환시키면서 반복
  visited = [[0] * n for i in range(n)] # 방문기록 0으로 초기화
  cnt = 0

  for j in range(n):
    for k in range(n):
      if graph[j][k] > i and visited[j][k] == 0: # 물 높이 i보다 높으면서 방문 안 한 곳
        bfs(j, k, i, visited) # bfs 다 돌고
        cnt += 1 # 카운트 1 증가

  if result < cnt: # result 업데이트
    result = cnt
 
print(result)