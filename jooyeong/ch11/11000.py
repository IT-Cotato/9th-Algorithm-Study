import heapq
import sys

n = int(sys.stdin.readline())
arr = []
heap = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: x[0])

cnt = int(1)
heapq.heappush(heap, arr.pop(0)[1])

for x in arr:
    if x[0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, x[1])
    else:
        heapq.heappush(heap, x[1])
        cnt += 1

print(cnt)