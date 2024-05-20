n = int(input())
schedule = []

for i in range(n):
  schedule.append(list(map(int,input().split())))

dp = [0 for i in range(n+1)] # 최대 수익

for i in range(n):
  for j in range(i + schedule[i][0], n + 1): # i번째 날에 상담할 때, 상담이 가능한 모든 날짜. (i + 상담 기간) <= j <= 마지막 날(n)
    if dp[j] < dp[i] + schedule[i][1]: # i번째 날에 상담할 때, 수익이 더 크면 상담 진행하기 
      dp[j] = dp[i] + schedule[i][1] # -> dp에 넣기

print(dp[-1]) # 마지막 날 수익