n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort() # 입력받은 수 정렬
big1 = num[n-1] # 가장 큰 수
big2 = num[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * big1 # 가장 큰 수 덧셈
result += (m-count) * big2 # 두 번째로 큰 수 덧셈

print(result)