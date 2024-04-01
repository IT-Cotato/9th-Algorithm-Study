# 숫자 카드 게임

# 각 행에서 가장 작은 숫자 중에서 가장 큰 숫자 찾으면 됨

a, b = map(int, input().split())    # 행, 열

min_list = []

for i in range(a):
    row = list(map(int, input().split()))
    min_list.append(min(row))

print(max(min_list))