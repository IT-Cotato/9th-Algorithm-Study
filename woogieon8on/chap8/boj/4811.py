import sys
input = sys.stdin.readline

# w: 한 조각 | h: 반 조각
dp = [[0 for _ in range(31)] for _ in range(31) ] # 행: 남은 w의 개수 | 열: 남은 h의 개수 -> dp[i][j]: w i개와 h j개로 만들 수 있는 경우의 수

for j in range(1,31): # h만 남은 경우
    dp[0][j] = 1 # h를 먹는 방법만 존재하기 때문에 경우의 수는 1

for i in range(1,31):
    for j in range(30):
        if j == 0: # w만 남은 경우
            dp[i][j] = dp[i-1][j+1] # w를 먹으면 h가 반드시 하나 생성 -> w-1 | h+1
        else: # h가 하나라도 있는 경우
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1] # w를 먹으면 h가 하나 생성 -> w-1 | h+1
                                                 # h를 먹으면 w는 그대로, h 하나 감소 -> w | h-1
                                                 # 두 경우의 수를 더함

while True:
    n = int(input())
    if n == 0: # 입력 종료
        break
    print(dp[n][0])