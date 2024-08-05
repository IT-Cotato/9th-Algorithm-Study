import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0] * (n+1) for i in range(n+1)] # 친구 관계 그래프
visited = [0 for _ in range(n+1)] # 방문 여부 -> 상근이와의 거리

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque([x]) # x: 시작점
    visited[x] = 1

    while queue:
        friend_num = queue.popleft()
        for people_num in graph[friend_num]: # 해당 친구에게 연결된 모든 사람에 대해
            if visited[people_num] == 0: # 아직 방문하지 않은 경우
                queue.append(people_num) # 큐에 추가
                visited[people_num] = visited[friend_num] + 1 # 상근이로부터의 거리 기록

bfs(1) # 1번 인덱스: 상근이
result = 0
for i in range(2, n+1):
    if 0 < visited[i] <= 3: # 상근이로부터의 거리가 3 이하인 친구들만 추가
        result += 1
        
print(result)