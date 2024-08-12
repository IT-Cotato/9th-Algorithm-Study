n = int(input())

dp = [[0] * 10 for _ in range(n + 1)] # 0으로 초기화

for i in range(1, 10): # 길이가 1인 계단 수 (dp[1][1] ~ dp[1][9]) - 1로 초기화
  dp[1][i] = 1

mod = 1000000000

# 길이가 2 이상인 계단 수
for i in range(2, n + 1):
  for j in range(10): # 0 ~ 10
    if j == 0: # j가 0일 때
      dp[i][j] = dp[i - 1][1] # 이전 자리수가 1만 가능
    elif j == 9: # j가 9일 때
      dp[i][j] = dp[i - 1][8] # 이전 자리수가 8만 가능
    else: # j가 1~8일 때 
      dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] # 이전 자리수가 -1, +1 만 가능

print(sum(dp[n]) % mod) # 길이가 n인 모든 계산 수 합산 % 1000000000