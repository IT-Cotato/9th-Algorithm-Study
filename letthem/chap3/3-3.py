n, m = map(int, input().split())

num = 0

# 각 행을 입력받아 min값과 num 비교

for i in range(n): # 열(n) -> 행마다 반복
	num_list = list(map(int, input().split()))
	candidate = min(num_list) # 해당 행의 min 값을 candidate로
	num = max(num, candidate) # num값과 candidate값 max 비교

print(num)
