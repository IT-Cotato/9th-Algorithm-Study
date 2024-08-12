from collections import deque

# BFS 함수 정의
def bfs(x, y, height, visited, graph):
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 최대 안전 영역 개수
result = 0

# 강수량을 0부터 100까지 변화시키며 안전영역을 계산
for height in range(101):
    visited = [[False] * N for _ in range(N)]
    safe_areas = 0
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and visited[i][j] == False:
                bfs(i, j, height, visited, graph)
                safe_areas += 1
                
    result = max(result, safe_areas)
    
print(result)