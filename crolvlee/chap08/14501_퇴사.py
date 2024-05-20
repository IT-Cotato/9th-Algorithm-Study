N = int(input())
T = []
P = []
max_value = 0

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    time = T[i] + i

    if (time <= N):     # 상담 기간 안에 끝나는 경우
        dp[i] = max(P[i] + dp[time], max_value)
        max_value = dp[i]
    else:   # 상담 기간 안에 끝나지 않는 경우
        dp[i] = max_value

print(max_value)