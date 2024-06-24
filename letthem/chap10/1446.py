import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미

n , d = map(int,input().split()) # n: 지름길의 개수 d: 고속도로의 길이
graph = [[] for _ in range(d + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트, d + 1은 1부터 시작하므로
distance = [INF] * (d + 1) # 거리 무한으로 모두 초기화

#일단 거리 1로 초기화. (ex. 노드가 0 ~ 150까지 이어져있음. 1->2, 149->150 등. 지름길이 없으면 이게 최단거리가 됨)
for i in range(d):
    graph[i].append((i + 1, 1)) # i에서 i + 1까지 거리는 1이라고 초기화

#지름길 있는 경우에 업데이트
for _ in range(n):
    s, e, l = map(int,input().split()) # s: start, e: end, l: start~end 지름길 거리
    if e > d: # 목적지보다 멀리 있으면 뒤로 못 돌아오니 무시.
        continue
    graph[s].append((e, l))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 : 0 으로 초기화
    heapq.heappush(q, (0, start)) # (거리, 노드). (ex. '노드'까지의 '거리')
    distance[start] = 0 # 최단 거리 테이블에 start에 0 삽입

    # q가 있다면 - 힙에 원소가 없을 때까지 반복 !!
    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보(거리, 노드) 꺼내기 

        if dist > distance[now]: # 현재 테이블과 비교하여 가중치가 더 큰 튜플이면 무시
            continue

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1] # graph[now] 기준으로 i가 도니까 i[0]: e, i[1]: l
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]: # 합한 거리가 다음 노드(end)까지 가는 거리보다 짧은 경우에 업데이트 !
                distance[i[0]] = cost # 업데이트
                heapq.heappush(q,(cost, i[0])) # (거리, 노드)

# 다익스트라 수행
dijkstra(0)
# 거리의 최솟값 출력
print(distance[d])