from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

# 가중치 없는 방향 그래프
graph = [list(map(int, input().split())) for _ in range(n)]

# 출력 행렬
matrix = [[0]*n for _ in range(n)]

def bfs(x): # x: 시작점

    queue = deque([x])
    visited = [False for _ in range(n)] # 방문 여부 리스트 초기화

    while queue:
        v = queue.popleft()

        for i in range(n): # 현재 정점 v와 연결된 모든 정점 확인
            if not visited[i] and graph[v][i] == 1: # 정점 i를 방문하지 않았고, v에서 i로의 간선이 존재하는 경우
                queue.append(i) # 큐에 추가
                visited[i] = True # 방문 표시
                matrix[x][i] = 1 # 출력 행렬에 1 표시

for i in range(n): # 각 정점에서 BFS 수행
    bfs(i)

for i in matrix: # 정답 행렬 출력
    print(*i)