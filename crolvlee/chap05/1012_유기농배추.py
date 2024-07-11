import sys
sys.setrecursionlimit(10000) # 재귀의 최대 높이 설정

def dfs(x, y):
    # 상, 하, 좌, 우 확인을 위한 dx, dy 생성
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # 현재 위치 방문 처리
    ground[y][x] = -1

    # 상, 하, 좌, 우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):     # 옭긴 위치가 ground 안에 있을 때
            if ground[ny][nx] == 1:             # 배추가 있다면
                dfs(nx, ny)                     # 옮긴 위치에서 재귀 호출


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    # ground에 다 0으로 초기화
    ground = [[0] * M for _ in range(N)]

    # 배추가 있는 위치에 1로 표시 
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    # 인접해 있는 배추 그룹
    count = 0
    
    # DFS로 배추 그룹을 세기
    for b in range(N):          # N은 세로
        for a in range(M):      # M은 가로
            if ground[b][a] == 1:
                dfs(a, b)
                count += 1

    print(count)