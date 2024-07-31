import heapq

N = int(input())

# 우선순위 큐 - 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있음 -> heap 자료구조
heap = []
for i in range(N):
  cards = int(input()) # N번만큼
  heapq.heappush(heap, cards)

total = 0

# 가장 작은 묶음 두 개씩 찾아서 더해주고 그 새로 만들어진 묶음을 다시 큐에 넣는다
while len(heap) > 1:
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)

  sum_value = one + two
  total += sum_value
  heapq.heappush(heap, sum_value)

print(total)
