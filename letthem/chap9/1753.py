import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input()) # 시작 노드 번호
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 (u - 출발, v - 도착, w - 가중치)

# 모든 간선 정보 입력 받기 (u, v, w)
for i in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

distance = [INF] * (n + 1) # 최단 거리 테이블을 모두 무한으로 초기화

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start)) # (거리, 노드)
  distance[start] = 0 # 최단 거리 테이블에 start에 0 삽입

  while q: # q가 있다면
    dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보(거리, 노드) 꺼내기 
    if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 distance에 삽입되어 있을테니 무시하기
      continue
    for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]: # i[0]은 노드 번호. cost는 거리
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) # (거리, 노드)

# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1): # 1 ~ n
  if distance[i] == INF:
    print("INF")
  # 도달할 수 있는 경우 거리 출력
  else:
    print(distance[i])