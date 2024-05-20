n = int(input())
dp = []

for i in range(n):
  dp.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(0, i+1):
    if j == 0: 
      dp[i][0] += dp[i-1][0] # 0열끼리 더하기
    elif j == i: 
      dp[i][j] += dp[i-1][j-1] # i열끼리 더하기
    else: # 그 외
      dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) # 위에서 오는 수 중 큰 수

print(max(dp[n-1])) # 가장 마지막 행(다 더해진 행)에서 가장 큰 수
    