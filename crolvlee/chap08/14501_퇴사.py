N = int(input())
T = []
P = []
max_value = 0   #뒤에서부터 계산할 때, 현재까지의 최대 상담 금액

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (N+1)    # dp[i]는 i번재 날부터 마지막 날까지 낼 수 있는 최대 이익

for i in range(N-1, -1, -1):
    time = T[i] + i

    # 상담 기간 안에 끝나는 경우
    if (time <= N):
        dp[i] = max(P[i] + dp[time], max_value) # max(현재 상담 일자의 이윤 + 현재 상담을 마친 일자부터의 최대 이윤, 뒤에서부터 계살할 때 현재까지의 최대 상담 금액)
        max_value = dp[i]
    # 상담 기간 안에 끝나지 않는 경우
    else:
        dp[i] = max_value

print(max_value)
