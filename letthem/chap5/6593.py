import sys
input = sys.stdin.readline
from collections import deque

# 3차원 방향 벡터
dz = (1, -1, 0, 0, 0, 0)
dx = (0, 0, 1, -1, 0, 0)
dy = (0, 0, 0, 0, 1, -1)


while True:
  l, r, c = map(int, input().split()) # 층, 행, 열
  if l == 0 and r == 0 and c == 0: # 0 0 0 만나면 탈출
    break
  board = [] # 3차원 미로 저장하는 리스트
  visited = [[[False] * c for _ in range(r)] for _ in range(l)] # 방문기록 false로 초기화
  for _ in range(l):
    board.append([list(input().strip()) for _ in range(r)]) # 각 층 정보 입력받기
    temp = input() # 빈 줄 -> 층 나누기

  q = deque()
  escaped = False

  for i in range(l):
    for j in range(r):
      for k in range(c):
        if board[i][j][k] == 'S': # start
          start = (i, j, k, 0)
          visited[i][j][k] = True
        if board[i][j][k] == 'E': # end
          goal = (i, j, k)

  # bfs 탐색
  q.append(start)
  while q:
    # print(f'cur q: {q}')
    z, x, y, d = q.popleft()
    if (z, x, y) == goal:
      escaped = True
      print(f'Escaped in {d} minute(s).')
      break
    nd = d + 1

    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny]:
        if board[nz][nx][ny] == '.' or board[nz][nx][ny] == 'E':
          q.append((nz, nx, ny, nd)) # bfs 이어서 진행 ..
          visited[nz][nx][ny] = True

  if not escaped:
    print('Trapped!')