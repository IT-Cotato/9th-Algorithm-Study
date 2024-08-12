import sys
input = sys.stdin.readline

n = int(input()) # 회원의 수
arr = [[n] * n for _ in range(n)] # 친구 관계 입력 받는 배열
dist = [0] * n # 각 정점별 가장 먼 거리에 대한 거리 표

for i in range(n):
  for j in range(n):
    if i == j:
      arr[i][j] = 0 # 자기 자신과의 거리는 0
while 1:
  a, b = map(int, input().split()) # arr에 친구 관계 삽입
  if [a, b] == [-1, -1]: # -1, -1 이면 stop
    break
  arr[a - 1][b - 1] = 1
  arr[b - 1][a - 1] = 1


# 플로이드-와샬 알고리즘
for k in range(n): # k : 중간지점
  for i in range(n):
    for j in range(n):
      arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]) # 중간 지점을 통해 이동하는 거리가 더 짧으면 갱신

# 각 정점별로 가장 먼 거리를 입력
for i in range(n):
  dist[i] = max(arr[i])

# 그 중 가장 작은 값(후보의 점수)
t = min(dist)

print(t, dist.count(t)) # 후보의 점수와, 그 후보의 수
for i in range(n):
    if dist[i] == t:
        print(i + 1, end=" ") # 후보 번호 : 인덱스니까 + 1해서 출력