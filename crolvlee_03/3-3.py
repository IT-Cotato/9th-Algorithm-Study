# 1이 될 때까지

n, k = map(int, input().split())

count = 0

while n > 1:
    if n % k != 0:  # 1. n을 1로 빼는 경우
        n -= 1
        count += 1
    else:           # 2. n을 k로 나누는 경우
        n /= k
        count += 1

print(count)
