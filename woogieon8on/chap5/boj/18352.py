from collections import deque

n, m, k, x = map(int, input().split())

graph = {} # node, edge로 구성된 2차원 배열 생성
distance = {} # 거리 배열 생성
visited = {} # 방문 유무 배열 생성
for i in range(n+1):
    graph[i] = []
    distance[i] = 0
    visited[i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs 알고리즘 구현
def bfs(start):
    nodes = []
    queue = deque([start]) # 큐 구현 위해 deque 라이브러리 사용!
    distance[start] = 0 # 출발 도시로부터의 거리: 0
    visited[start] = 1

    while queue:
        now = queue.popleft() # deque: 앞 뒤로 요소를 추가하고 삭제할 수 있는 자료구조
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i) # 현재 노드가 방문한 노드 queue에 추가
                distance[i] = distance[now] + 1
                if distance[i] == k: # 최단 거리가 k인 노드 출력에 추가
                    nodes.append(i)

    if len(nodes) == 0: # 출력할 노드가 하나도 존재하지 않으면 -1 출력
        print(-1)
    else:
        nodes.sort() # 출력 노드 오름차순 정렬
        for i in nodes:
            print(i)

bfs(x) # 출발 노드 x