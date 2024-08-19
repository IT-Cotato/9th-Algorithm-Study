import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [[] for _ in range(N+1)] # 도시 정보 리스트

for i in range(M):
    a, b, cost = map(int, input().split())
    arr[b].append([a, cost]) # b 도시에서 a 도시로 이동하는 비용이 cost

targets = list(map(int, input().split())) # 면접장 정보 리스트

def dijkstra():
    h = [] # 최소 힙 생성

    # 모든 면접장을 시작점으로 설정
    for t in targets:
        heapq.heappush(h, [0, t]) # 면접장 도시는 거리 0으로 시작
        result[t] = 0

    while h:
        cost, city = heapq.heappop(h) # 현재 힙에서 가장 작은 비용의 도시 꺼냄

        if result[city] < cost: # 각 도시에 대한 최단 거리 정보가 현재 비용보다 적은 경우 무시
            continue

        for next_city, next_cost in arr[city]: # 현재 도시에서 이동할 수 있는 모든 도시
            if cost + next_cost < result[next_city]: # 더 짧은 비용 갱신
                result[next_city] = cost+next_cost
                heapq.heappush(h, [cost+next_cost, next_city]) # 힙에 추가

max_start, max_cost = 0, 0 # 가장 먼 도시, 그 거리

result = [int(1e11)] * (N+1) # 결과 초기값 매우 큰 수(도달할 수 없는 경우)로 설정

dijkstra() # 면접장에서 다른 도시로 가는 최단 거리 계산

for i, r in enumerate(result): # enumerate(): 리스트의 각 요소와 그 요소의 인덱스 함께 반환
    if r > max_cost and r != int(1e11): # 가장 큰 값 갱신(도달할 수 없는 경우 제외)
        max_start, max_cost = i, r

# 면접장에서 가장 먼 도시와 그 거리 출력        
print(max_start)
print(max_cost)