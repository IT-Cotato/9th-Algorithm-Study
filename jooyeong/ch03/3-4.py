# 이것이 코딩테스트다 3장 1이 될 때까지

n, k = map(int, input().split())

count = 0
while n != 1: # n이 1이 아닐 때 연산 수행
    if n % k == 0:
        n = n / k
        # n이 k로 나누어떨어지는 경우, 두 번째 조건에 따라 n을 k로 나눔
    else:
        n -= 1
        # n이 k로 나누어떨어지지 않는 경우, 첫 번째 조건에 따라 n에서 1을 뺌
    count += 1
    # 위 연산을 반복하며 n이 1이 될 때까지 과정을 몇 번 수행해야 하는지 구함

print(count)