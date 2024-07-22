import sys
input = sys.stdin.readline

arr = [[0] * 31 for _ in range(31)]

# i = i개의 알약, j = j개의 반 조각짜리 알약
for i in range(1, 31):
  arr[0][i] = 1 # 1개짜리 알약 먹는 건 하루에 경우의 수가 한 가지다!

for i in range(1, 31):
  for j in range(i, 31):
    arr[i][j] = arr[i-1][j] + arr[i][j-1] # 현재 = 왼쪽 + 위쪽

while True:
  n = int(input())
  if n == 0:
    break
  print(arr[n][n])