import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

# 각 도시에 연결되어 있는 도시에 대한 정보를 담는 이차원 리스트
graph = [[] for i in range(N + 1)]
# graph = [
#         []
#         [(2, 2), (3, 3), (4, 1), (5, 10)]
#         [(4, 2)]
#         ]

# 방문한적이 있는 도시를 체크하기 위한 리스트
visited = [False] * (N + 1)

# 최단 거리 테이블 -> 무한대로 초기화
distance = [INF] * (N + 1)

# graph에 정보 채우기
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 출발점의 도시번호와 도착점의 도시번호
start, end = map(int, input().split())

# 다익스트라 함수
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # 큐에 (비용, 도시번호)가 들어감
    distance[start] = 0             # 최단거리 테이블 시작노드는 0으로

    while q:
        # 가장 최단거리가 짧은 도시에 대한 정보 꺼내기
        curCost, curNode = heapq.heappop(q)

        # 테이블에 있는 값보다 큐에 있는 비용이 크다면, 이미 방문한 노드임
        if distance[curNode] < curCost:
            continue
            
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[curNode]:
            cost = curCost + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
# 다익스트라 알고리즘 수행
dijkstra(start)

print(distance[end])