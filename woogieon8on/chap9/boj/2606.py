from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

# 네트워크 구성 그래프
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    queue = deque([x]) # x: 시작점
    count = 0
    visited[x] = True # 시작점 방문 표시

    while queue:
        node = queue.popleft()
        for next_node in graph[node]: # 현재 컴퓨터에 연결된 모든 컴퓨터
            if not visited[next_node]: # 방문하지 않은 컴퓨터인 경우
                visited[next_node] = True # 방문 표시
                queue.append(next_node) # 큐에 추가
                count += 1 # 감염된 컴퓨터 수 증가

    return count

visited = [False for _ in range(v+1)] # 방문 여부 리스트 초기화
print(bfs(1)) # 시작점: 1