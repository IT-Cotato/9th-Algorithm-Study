import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split()) # 도시의 수, 도로의 수, 면접장의 수
arr = [[] for _ in range(n + 1)]
for i in range(m): # 도로 수만큼 돌면서 출발도시, 도착도시, 거리 입력받기
  a, b, cost = map(int, sys.stdin.readline().split())
  arr[b].append([a, cost]) # 도착도시에 출발도시와 거리 넣어주기. 역방향으로. arr에 도시의 정보 넣음
# 모든 경우의 수 연산하면 시간 초과 발생하기 때문.
# 모든 도시에서 면접장으로 갈 수 있는 경로가 항상 있다 -> 거꾸로 면접장에서 도시로 향하는 방향으로 다익스트라 수행하자
targets = list(map(int, sys.stdin.readline().split())) # 면접장 정보는 마지막 줄. target에 입력받기


def dijkstra():
  h = [] # 힙 초기화
  for t in targets:
    heapq.heappush(h, [0, t]) # 힙에 면접장 push 해놓기
    result[t] = 0 # 면접장까지의 거리는 0으로 초기화
  while h: # h에 값이 들어있는 동안 반복
    cost, city = heapq.heappop(h) # heapq.heappop(h)는 우선순위 큐 h에서 가장 작은 비용과 해당 도시를 꺼냄 -> 해당 도시에서 도달할 수 있는 다른 도시들의 비용을 갱신함
    if result[city] < cost: # 현재 꺼낸 거리 cost가 이미 기록된 거리 result[city]보다 크다면 무시.
      continue
    for next_city, next_cost in arr[city]: # 현재 꺼낸 거리 cost가 더 작다면 현재 도시에서 연결된 모든 다음 도시와 거리를 순회
      if cost + next_cost < result[next_city]: # 원래 거보다 작다면 result 업데이트
        result[next_city] = cost + next_cost
        heapq.heappush(h, [cost + next_cost, next_city]) # h에 거리와 도시 push


max_start, max_cost = 0, 0 # 가장 먼 도시와 거리 0으로 초기화
result = [int(1e11)] * (n + 1) # result에 최대한 큰 값을 넣어 초기화
dijkstra() # 다익스트라 수행

for i, r in enumerate(result): # enumerate: result 리스트의 각 요소에 대해 인덱스 i와 값 r을 함께 반환
  if r > max_cost and r != int(1e11): # 가장 먼 도시와 거리 업데이트
    max_start, max_cost = i, r
print(max_start)
print(max_cost)