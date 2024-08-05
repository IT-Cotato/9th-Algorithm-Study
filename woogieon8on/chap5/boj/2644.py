import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)] # 방문 횟수 -> 촌수

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, b):
    queue = deque([a])
    visited[a] = 0 # 시작 사람의 촌수 = 0

    while queue:
        people = queue.popleft()

        if people == b: # b: 목표 사람
                        # 큐에서 꺼낸 사람과 목표 사람이 일치하면 촌수 반환
            return visited[b]
        
        for i in graph[people]:
            if visited[i] == 0: # 아직 방문하지 않은 사람인 경우 큐에 추가
                queue.append(i)
                visited[i] = visited[people] + 1 # 해당 사람 촌수 1 중가시켜 촌수 배열에 저장

    return -1 # 촌수를 계산할 수 없는 경우 -1 반환

print(bfs(a, b))