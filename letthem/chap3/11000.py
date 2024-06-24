import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort() # 강의 시작 시간 기준으롤 정렬

# 힙에는 종료시간을 넣음.
heap = [time[0][1]] # 제일 처음 시작하는 강의의 종료시간을 넣어 초기화
for i in range(1, n):
    if heap[0] <= time[i][0]: # 힙에 들어있는 강의의 종료시간보다 i번째 강의의 시작시간이 크거나 같으면, i번째 강의를 같은 강의실에서 수강 가능
        heapq.heappop(heap) # 원래 있던 강의를 pop하고
    heapq.heappush(heap,time[i][1]) # 새로 들어온 i번째 강의의 종료시간을 push.

print(len(heap)) # 힙의 크기(= 개수)가 강의실의 개수가 됨
