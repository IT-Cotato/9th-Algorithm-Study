import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

v, e = map(int, input().split()) # v 노드의 개수, e 간선의 개수
k = int(input()) # k 시작 노드 번호

graph = [[] for i in range(v + 1)] # 노드 간의 거리에 대한 정보를 담은 그래프를 만든 후
distance = [INF] * (v + 1) # 노드의 거리를 모두 무한대로 초기화

for _ in range(e):
    a, b, c = map(int, input().split())
    # 문제에 제시된 변수는 u, v, w이지만 노드의 개수를 의미하는 변수 V와 혼동돼서 a,b,c로 작성함
    graph[a].append((b, c))
    # 노드 a에서 노드 b로 가는 비용이 c

def dijkstra(start):
    q = []
    # 우선순위 큐 사용
    heapq.heappush(q, (0, start))
    # heapq 라이브러리 - 원소로 튜플을 입력받으면 튜플의 첫 번째 원소를 기준으로 우선순위 큐 구성
    # (거리, 노드번호) 순으로
    # 우선순위 큐에 start의 거리를 0으로. 즉, 시작 노드로 가기 위한 최단 경로 0
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # 최단 거리가 가장 짧은 노드 정보를 꺼내고
        # (우선순위 큐를 사용하므로 거리가 가장 짧은 노드가 최상위 원소로 위치함)
        if distance[now] < dist:
            continue
            # 이미 처리된 적 있는 노드라면 무시
        for i in graph[now]:
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
        # 경로가 없는 경우
    else:
        print(distance[i])
        # 경로가 있는 경우