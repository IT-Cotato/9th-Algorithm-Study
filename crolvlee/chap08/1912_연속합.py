n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n   # arr[i]까지 고려했을 때 최대 연속합. 원소는 모두 0으로 초기화해주기

dp[0] = arr[0]

for i in range(1, n):
    # 지금 현재 값 or 이전 최대 연속값 + 현재 값
    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))
