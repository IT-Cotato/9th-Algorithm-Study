N = int(input())

cards = []
for _ in range(N):
    cards.append(int(input()))

cards.sort() # 카드 묶음 오름차순 정렬

compare = 0
i = 0
while i < (N - 1):
    if i == 0:
        compare = cards[i] + cards[i + 1]
    else:
        compare += compare + cards[i + 1] # 작은 묶음부터 합치기
    i = i + 1

print(compare)