n, k = map(int, input().split())

count = 0
while True:
    if n % k != 0: # n이 k로 나누어 떨어지지 않는 경우
        n -= 1
        count += 1
        if n == 1: # n이 1이 되면 종료
            break
    elif n % k == 0: # n이 k로 나누어 떨어지는 경우
        n /= k
        count += 1
        if n == 1: # n이 1이 되면 종료
            break

print(count)