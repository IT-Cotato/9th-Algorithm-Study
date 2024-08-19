import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

# 최소 힙 생성
cards = []

card_list = [int(x) for x in input().split()]
for card in card_list:
    heapq.heappush(cards, card)

for _ in range(m): # 카드 합체 m번 진행

    # 가장 작은 값을 가진 카드 꺼내기
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    # 두 카드를 더한 값을 각 카드에 덮어쓰기
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

# 최종적으로 남은 카드의 값들을 더해 결과 출력
print(sum(cards))