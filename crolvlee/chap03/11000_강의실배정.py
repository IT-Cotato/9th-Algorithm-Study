import heapq
import sys

N = int(input())
time_list = []

for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    time_list.append([S, T])

# 시작 시간, 끝나는 시간이 빠른 순으로 정렬
time_list.sort()

# 끝나는 시간을 힙에 추가
end_time_heap = []
end_time_heap.append(time_list[0][1])

for t in time_list[1:]:
    if end_time_heap[0] <= t[0]:
        heapq.heappop(end_time_heap)
    heapq.heappush(end_time_heap, t[1])

print(len(end_time_heap))