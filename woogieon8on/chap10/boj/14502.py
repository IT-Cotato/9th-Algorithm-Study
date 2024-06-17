from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 바이러스는 벽(1)을 제외한 모든 영역을 향하여 BFS를 통해 자신을 감염시킴
def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph) # 원래의 graph 유지

    # 바이러스(2)를 큐에 넣음
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    # 감염 시작
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 확인
                continue
            if tmp_graph[nx][ny] == 0: # 감염 가능 여부, 즉 해당 칸이 0인지 확인
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    # 안전 영역(0) 카운트
    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt) # 안전 영역 크기 최대값 갱신

# 벽을 세우고, 3개의 벽을 모두 세워 안전 영역이 확정되면 그 개수를 세기 위해 BFS 사용
def makeWall(cnt):
    if cnt == 3: # 3개의 벽을 모두 세우면 BFS 사용하여 바이러스 감염 시작
        bfs()
        return
    
    # 벽을 세우는 모든 경우의 수 검토(백트래킹)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 벽 설치 가능 여부 확인
                graph[i][j] = 1 # 벽 설치
                makeWall(cnt+1) # 두번째 벽 설치하기 위해 makeWall() 재귀 호출
                graph[i][j] = 0 # 벽 제거

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)