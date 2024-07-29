import sys
input = sys.stdin.readline

# 지방의 수 : n, 각 지방의 예산 요청 : list, 총 예산 : m
n = int(input())
list = list(map(int, input().split()))
m = int(input())

result = 0  # 예산 상한액

start = 1
end = max(list)

# 이진 탐색
while start <= end:
  total = 0 # 지방들 예산의 합
  mid = (start + end) // 2 # 상한액 기준
  for i in list:
    if i > mid:
      total += mid # 상한액을 더한다
    else:
      total += i # list에 들어있는 값을 더한다
  if total <= m: # 총 예산 이하이면 중앙값을 늘린다
    result = mid
    start = mid + 1
  else: # 총 예산 초과이면 중앙값을 줄인다
    end = mid - 1

print(result)