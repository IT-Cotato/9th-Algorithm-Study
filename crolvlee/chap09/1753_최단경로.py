import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

V, E = map(int, input().split())    # 정점의 개수, 간선의 개수
K = int(input())                    # 시작 정점의 번호

INF = int(1e9)

# 그래프 초기화
graph = [[] * (V + 1) for _ in range(V + 1)]

# 최단거리는 모두 0으로 초기화
distance = [INF] * (V + 1)

# 간선 정보 입력
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

# 다익스트라 함수
def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)    # 최단거리가 가장 짧은 정점 정보 꺼내기

        if distance[now] < dist:        # 현재 정점이 이미 처리된 적 있다면 넘어가기
            continue

        # 현재 정점과 인접한 다른 정점들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(K)

# 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])