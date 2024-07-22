import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print('CY')
else:
    print('SK')

# # DP 활용
# N = int(input())
# dp = [0]*1001

# # SK == 0, CY == 1
# dp[1] = 0
# dp[2] = 1
# dp[3] = 0

# for i in range(4, N+1):
#     dp[i] = (dp[i-1] + 1) % 2  # N이 4 이상일 때, 승자는 이전 승자와 다른 사람

# print('SK' if dp[N] == 0 else 'CY')