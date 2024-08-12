import sys
input = sys.stdin.readline

def dfs(node, graph, visited):
    stack = [node]
    count = 0
    
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            count += 1
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    
    return count


# 입력 받음
n, m = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(A)
    
# 각 컴퓨터에서 해킹할 수 있는 컴퓨터 수를 계산
max_hack_count = 0
result = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    hack_count = dfs(i, graph, visited)
    if hack_count > max_hack_count:
        max_hack_count = hack_count
        result = [i]
    elif hack_count == max_hack_count:
        result.append(i)

# 결과 출력
result.sort()
print(' '.join(map(str, result)))