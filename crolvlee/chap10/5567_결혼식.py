# 1번 노드부터 탐색

# dfs함수
def dfs(graph, current, visited, depth):
    if depth > 2:   # 친구의 친구까지만 초대할 거니까
        return
    
    visited[current] = True     # 현재 노드를 방문 처리
    
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, depth+1)


# 입력 받음
n = int(input())    # 동기의 수
m = int(input())    # 리스트의 길이

# 각 노드가 연결된 정보
graph = [[] for _ in range(n+1)]

# 각 노드가 방문된 정보를 리스트로 표현
visited = [False] * (n+1)

# graph에 연결된 정보 담음
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

# dfs 수행
dfs(graph, 1, visited, 0)

invite_count = visited.count(True) - 1  # 1번 노드(본인) 제외하고 카운트
print(invite_count)