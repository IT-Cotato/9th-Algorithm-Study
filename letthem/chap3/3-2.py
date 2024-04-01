n, m = map(int, input().split())

num = 0

# 각 행을 입력받아 min값과 num 비교

for i in range(n):
	num_list = list(map(int, input().split()))
	candidate = min(num_list)
	num = max(num, candidate)

print(num)
