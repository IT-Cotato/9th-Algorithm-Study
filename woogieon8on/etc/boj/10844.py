import sys
input = sys.stdin.readline

n = int(input())

# DP 테이블 초기화
# d[i][j]: i자리 숫자 중 마지막 자릿수가 j인 계단 수의 개수
d = [[0] * 10 for _ in range(n+1)]

for i in range(1, 10):
    d[1][i] = 1 # 한 자리 숫자의 경우(1~9) 각 숫자는 자체로 계단 수
    
for i in range(2, n+1):
    for j in range(10): # j: 마지막 자릿수(0~9)
        if j == 0:
            d[i][j] = d[i-1][1] # 앞자리 수가 1인 경우만 가능
        elif 1 <= j <= 8:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1] # 앞자리 수가 j-1 또는 j+1인 경우 가능
        else:
            d[i][j] = d[i-1][8] # 앞자리 수가 8인 경우만 가능
            
print(sum(d[n]) % 1000000000) # n자리 계단 수의 총 개수를 1,000,000,000로 나눈 나머지