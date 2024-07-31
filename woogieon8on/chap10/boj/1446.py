import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())

graph = [[] for i in range(d+1)]
distance = [INF] * (d+1)

for i in range(d): # 고속도로 길이를 구성하는 0부터 d까지 모든 수를 각각 하나의 노드라고 가정
    graph[i].append((i+1, 1)) # 각 노드의 가중치 1로 설정

for _ in range(n): # 기존 그래프에 지름길 추가
    start, destination, length = map(int, input().split())
    if destination<=d: # 도착 지점이 고속도로 끝(d)보다 큰 경우는 제외
        graph[start].append((destination, length))

def dijkstra(start): # 다익스트라 알고리즘
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들 확인
            cost = distance[now] + i[1]
            if cost < distance[i[0]]: # 지름길을 거쳐 다른 노드로 이동할 때 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)

print(distance[d])