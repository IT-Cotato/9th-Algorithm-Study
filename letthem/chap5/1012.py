from collections import deque
import sys
input = sys.stdin.readline

d = [[1,0],[0,1],[-1,0],[0,-1]] # 상하좌우

def bfs(y, x):
    queue = deque()
    queue.append([y,x]) # q에 삽입
    visited[y][x] = True # 해당 좌표 방문처리

    while(queue):
        r, c = queue.popleft() # queue에서 꺼낸 현재 위치의 r: 행, c: 열

        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]

            if(0>dr or dr>=n or 0>dc or dc>=m): # 갈 수 없는 곳
                continue # 무시

            if ground[dr][dc] == 1 and not visited[dr][dc]: # 배추가 있고 방문한 적 없으면
                queue.append([dr,dc]) # q에 해당 좌표 삽입
                visited[dr][dc] = True # 해당 좌표 방문처리


t = int(input()) # 테스트 케이스의 개수

for _ in range(t):
    m, n, k = map(int,input().split()) # m : 가로 길이, n : 세로 길이, k : 배추의 개수

    ground = [[0] * m for _ in range(n)] # 0으로 다 채워 초기화
    visited = [[False] * m for _ in range(n)] # 방문 모두 안 한 걸로 초기화

    for i in range(k): # 배추 개수만큼
        x, y = map(int,input().split()) # 좌표 입력받기
        ground[y][x] = 1 # 배추 있는 곳에 1

    
    count = 0 # 배추흰지렁이 개수
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and not visited[i][j]: # 배추가 있고 방문한 적 없으면
                bfs(i,j) # bfs로 주변 방문처리하고
                count += 1 # 배추흰지렁이 1개 추가

    print(count) # 배추흰지렁이 개수 print