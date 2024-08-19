import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
high = 0

# 그래프 내에서 가장 높은 지점 찾기 -> 물의 높이 설정 기준
for i in range(N):
    for j in range(N):
        if graph[i][j] > high:
            high = graph[i][j]

dx, dy = [0,0,-1,1], [-1,1,0,0] # 이동 벡터

def bfs(i,j, high):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1 # 현재 위치 방문 처리

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 현재 위치에서 상하좌우로 이동 가능한 모든 위치 탐색
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위 벗어나는 경우 무시
                continue
            
            # 이동한 위치가 안전 영역인지 확인
            # 방문하지 않은 곳이라면 방문 처리 후 큐에 추가
            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

result = 0
for k in range(high):
    visited = [[0] * N for _ in range(N)] # 각 물의 높이에서 방문 여부 초기화
    ans = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0: # 현재 높이에서 안전한 영역 찾기
                bfs(i,j, k) # 연결된 영역 탐색
                ans += 1 # 안전 영역의 개수 증가
    
    if result < ans: # 가장 많은 안전 영역의 개수 갱신
        result = ans

print(result)