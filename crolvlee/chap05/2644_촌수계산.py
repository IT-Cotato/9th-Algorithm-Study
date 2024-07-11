from collections import deque

#bfs 함수
def bfs(start, end):
    queue = deque([start])
    visited[start] = 0  # 시작점의 촌수는 0
    
    while queue:
        current = queue.popleft()

        # 현재 노드가 목표 노도에 도달한 경우
        if current == end:
            return visited[current]
        
        # 인접한 노드를 방문하지 않은 경우
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)

    # 친척 관계가 없는 경우
    return -1


# 입력받음
n = int(input())                    # 전체 사람 수
a, b = map(int, input().split())    # 촌수 계산해야 하는 서로 다른 두 사람
m = int(input())                    # 부모-자식 관계의 개수

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 부모-자식 관계 입력받아 그래프에 채우기
# 예시: graph = [[], [], [4], [], [2]]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 여부와 촌수를 저장하는 리스트 초기화
visited = [-1] * (n+1)

# bfs를 이용하여 a와 b의 촌수 계산
result = bfs(a, b)

print(result)