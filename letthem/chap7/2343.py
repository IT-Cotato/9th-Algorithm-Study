import sys

# 강의의 수 : n , 블루레이 개수 : m
n, m = list(map(int, sys.stdin.readline().split()))
# 강의 개별 시간
array = list(map(int, sys.stdin.readline().split()))

# 블루레이의 크기 구해야 함

start = max(array) # 시작점 (모두 나눠졌을 때 -> 가장 큰 값)
end = sum(array) # 끝점 (모두 더한 값)

while(start <= end):
  total = 0
  mid = (start + end) // 2
  
  count = 1 # 블루레이 개수
  # 블루레이 개수 세기
  for i in array:
    if total + i > mid:
      count += 1
      total = 0
    total += i # mid 값 넘길 때까지 더하기
  
  # 블루레이 개수가 m보다 작거나 같으면 좀 더 작게 나눠지도록 끝점을 mid - 1로 이동시켜서 블루레이 개수 늘리기
  if count <= m:
    result = mid # 일단 현재 mid값으로 result
    end = mid - 1

  # 블루레이 개수가 m보다 많으면 좀 더 크게 나눠지도록 시작점을 mid + 1로 이동시켜서 블루레이 개수 줄이기
  else:
    start = mid + 1

    
print(result)
