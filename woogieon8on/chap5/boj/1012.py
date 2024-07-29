import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >=N or ny >= M: # 범위를 벗어나는 경우 무시
        continue

      if matrix[nx][ny] == 1: # 새로운 위치에 배추가 존재하는 경우 큐에 추가
        queue.append((nx,ny))
        matrix[nx][ny] = 0 # 0: 이미 방문한 셀

  return

for _ in range(T):
  M, N, K = map(int, input().split())
  matrix = [[0]*M for _ in range(N)]

  for i in range(K):
    x, y = map(int, input().split())
    matrix[y][x] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if matrix[i][j] ==1: # 배추가 존재하는 경우 bfs 호출
        bfs(i, j)
        cnt +=1 # bfs 호출할 때 마다 카운터 증가
                # 카운터: bfs 호출 횟수 -> 배추가 모여있는 구역의 개수

  print(cnt)