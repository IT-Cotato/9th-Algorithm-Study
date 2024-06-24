import heapq

N = int(input())

card_heap = []

for i in range(N):
    num = int(input())
    heapq.heappush(card_heap, num)

# card_heap = [60, 40, 50, 70]

# 총 비교 횟수
total_cost = 0

# 카드 묵음이 1개가 남을 때까지 반복
while len(card_heap) > 1:
    # 작은 두 묶음 합치기
    first_min = heapq.heappop(card_heap)
    second_min = heapq.heappop(card_heap)
    new_bundle = first_min + second_min

    # 총 비교 횟수에 합치기
    total_cost += new_bundle

    # 합친 새로운 묶음을 다시 힙에 추가
    heapq.heappush(card_heap, new_bundle)

print(total_cost)