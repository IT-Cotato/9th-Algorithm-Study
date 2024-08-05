# 한 조각을 꺼낸 날에는 w
# 반 조각을 꺼낸 날에는 h

import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]
# i: w의 개수
# j: h의 개수
# dp[i][j] -> w i개 / h j개로 만들 수 있는 경우의 수

# w가 없고 h만 남아 있다면 -> h만 선택 가능
for j in range(1, 31):
    dp[0][j] = 1

for i in range(1, 31):
    for j in range(0, 30):
        if j == 0:  # h가 하나도 없을 때 -> w를 1개 먹으면 h가 생김
            dp[i][j] = dp[i-1][j+1]
        else:       # h가 하나라도 있으면
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1]


while True:
    n = int(input())
    if (n == 0):
        break
    print(dp[n][0])

