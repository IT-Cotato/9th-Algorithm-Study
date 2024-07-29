N = int(input())

dp = [-1] * 1001
# dp[K] = 1이라면, K개의 돌이 있을 때 SK가 이긴다는 뜻
# dp[K] = 0이라면, K개의 돌이 있을 때 CY가 이긴다는 뜻

dp[1] = 1   # SK가 이김
dp[2] = 0   # CY가 이김
dp[3] = 1   # SK가 이김

for i in range(4, N+1):
    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N] % 2 == 1:
    print("SK")
else:
    print("CY")