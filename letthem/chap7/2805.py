import sys

# 나무의 수 : n , 가져가려는 나무의 길이 : m
n, m = list(map(int, sys.stdin.readline().split()))
# 나무들의 높이
array = list(map(int, sys.stdin.readline().split()))

start = 0 # 시작점
end = max(array) # 끝점

result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    # 잘랐을 때의 나무의 양 계산
    if x > mid:
      total += x - mid
  # 나무의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
  if total < m:
    end = mid - 1
  # 나무의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
    start = mid + 1
    
print(result)
