import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한

V, E = map(int, input().split())
start = int(input())

graph = [[] for i in range(V + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (V + 1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(E):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w인 간선 존재
    graph[u].append((v, w))

def dijkstra(start): # 다익스트라 알고리즘
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로 0 설정 + 큐에 삽입
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드 정보 꺼내기
        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐 다른 노드로 이동할 때 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF: # 경로가 존재하지 않는 경우
        print("INF")
    else:
        print(distance[i])