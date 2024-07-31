import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[]*(n+1) for _ in range(n+1)]
dist = [1E9]*(n+1)
heap = []

for _ in range(m):
    node1, node2, value = map(int,sys.stdin.readline().rstrip().split())
    graph[node1].append((value,node2))

start, destination = map(int,sys.stdin.readline().rstrip().split())

heapq.heappush(heap, [0, start])
dist[start] = 0

while heap:
    cost, node = heapq.heappop(heap)

    if cost > dist[node]:
        continue

    for i in graph[node]:
        nextCost, nextNode = i
        distance = nextCost + cost

        if dist[nextNode] > distance:
            dist[nextNode] = distance
            heapq.heappush(heap, [distance, nextNode])
        else:
            continue
print(dist[destination])