import sys
from collections import deque
input = sys.stdin.readline

# 이동 방향 (동,서,남,북,상,하)
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(x, y, z, e1, e2, e3):
    que = deque() 
    que.append((x, y, z))  # 시작 지점 큐에 추가
    visited[x][y][z] = 0  # 시작 지점 방문 표시 및 거리 0으로 초기화
    
    while que:
        x, y, z = que.popleft()  # 큐에서 현재 위치 꺼냄
        
        if x == e1 and y == e2 and z == e3: # 현재 위치가 종료 지점과 동일한 경우
            return visited[x][y][z] # 현재 위치 반환
        
        # 6개의 방향으로 이동 시도
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < s and 0 <= ny < n and 0 <= nz < m: # 범위 확인
                if visited[nx][ny][nz] == -1 and (maps[nx][ny][nz] == '.' or maps[nx][ny][nz] == 'E'): # 방문하지 않았고, 이동할 수 있는 위치인 경우
                    que.append((nx, ny, nz))  # 큐에 다음 위치 추가
                    visited[nx][ny][nz] = visited[x][y][z] + 1  # 이동 거리를 기록
    
    return -1 # 종료 지점에 도달하지 못한 경우

while True:
    
    s, n, m = map(int, input().split())
    
    if s == 0 and n == 0 and m == 0: # 종료 조건
        break
    
    visited = [[[-1 for _ in range(m)]for _ in range(n)]for _ in range(s)] # 방문 배열(-1: 방문하지 않음)
    
    maps = [] # 미로의 각 층을 저장할 배열
    
    for _ in range(s):
        temp1 = []
        for i in range(n + 1):
            temp2 = list(input().rstrip('\n')) # 줄 바꿈 문자 제거
            if i != n:  # 마지막 줄은 공백 줄이므로 제외
                temp1.append(temp2)
        maps.append(temp1)
    
    for i in range(s):
        for j in range(n):
            for k in range(m):
                if maps[i][j][k] == 'S':
                    x, y, z = i, j, k  # 시작 지점
                elif maps[i][j][k] == 'E':
                    e1, e2, e3 = i, j, k  # 종료 지점
    
    time = bfs(x, y, z, e1, e2, e3) # BFS 호출하여 탈출 시간 계산
    
    if time == -1:
        print("Trapped!")  # 탈출할 수 없는 경우
    else:
        print("Escaped in", time, "minute(s).")  # 탈출에 성공한 경우