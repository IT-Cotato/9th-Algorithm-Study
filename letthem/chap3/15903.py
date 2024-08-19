from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())

cards = [int(x) for x in stdin.readline().split()] # 리스트 컴프리헨션
# cards 리스트를 heap으로 변환
heapq.heapify(cards)

for _ in range(m):
  card1 = heapq.heappop(cards) # 가장 작은 값 pop
  card2 = heapq.heappop(cards) # 두 번째로 가장 작은 값 pop

  # 합친 걸 2번 push
  heapq.heappush(cards, card1 + card2)
  heapq.heappush(cards, card1 + card2) 

print(sum(cards))