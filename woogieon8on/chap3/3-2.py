n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort() # 입력받은 수 정렬
big1 = num[n-1] # 첫 번째로 큰 수
big2 = num[n-2] # 두 번째로 큰 수

sum = 0
count = 0

while count < m: # 숫자가 더해지는 횟수 m
    for i in range(k): # 첫 번째로 큰 수 k번 덧셈
        sum += big1
        count += 1
    sum += big2 # 두 번째로 큰 수 덧셈
    count += 1

print(sum)