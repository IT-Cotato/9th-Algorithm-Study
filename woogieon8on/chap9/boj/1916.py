from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 버스 노선 그래프
INF = 1e9
dp = [INF for _ in range(n + 1)] # 도시에 도착하는 최소비용 리스트

for i in range(m):
    s, e, cost = map(int, input().split()) # 버스 노선 - 시작 도시, 도착 도시, 버스 비용
    graph[s].append((e, cost))

start, target = map(int, input().split()) # 출발점, 목적지

def dijkstra(x): # x: 출발점

    dp[x] = 0 # 출발점의 도착 비용은 0
    heap = []
    heappush(heap, [0, x]) # [비용, 출발점] 힙에 push

    while heap:
        cost, point = heappop(heap)

        if dp[point] < cost: # 최소 비용 리스트의 해당 도시 비용이 더 적다면 무시
            continue

        for t, v in graph[point]: # 해당 좌표에서 출발하는 모든 버스 노선
            new_cost = cost + v # 지금까지의 비용 + 해당 노선 경로

            if dp[t] > new_cost: # 최소 비용 리스트에 저장된 도착 도시까지의 비용보다 계산된 비용이 더 적은 경우
                dp[t] = new_cost # 최소 비용 갱신
                heappush(heap, [new_cost, t]) # [계산된 비용, 도착 도시] 힙에 push

dijkstra(start) # 출발점으로부터 다익스트라 알고리즘 적용
print(dp[target]) # 목적지 최소 비용 값 출력