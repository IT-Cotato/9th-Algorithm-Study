import sys
import heapq
imput = sys.stdin.readline

n = int(input())
time = [] # 강의 시간 정보 리스트

for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x: (x[0], x[1])) # 강의 시작하는 시간 기준으로 정렬

heap = [time[0][1]] # 첫 번째 강의의 종료 시간 힙에 추가
for i in range(1,n):
    # heap[0]: 가장 빨리 끝나는 강의의 종료 시간
    # time[i][0]: 현재 강의의 시작 시간
    # 가장 빨리 끝나는 강의의 종료 시간보다 현재 강의의 시작 시간이 크거나 같은 경우
    # -> 강의실 재사용 가능
    if heap[0] <= time[i][0]:
        # 힙에서 가장 빨리 끝나는 강의의 종료 시간 제거
        # 현재 강의의 종료 시간 힙에 추가하여 가장 빨리 끝나는 강의의 종료 시간 업데이트
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap)) # 필요한 강의실 수