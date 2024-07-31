import sys
input = sys.stdin.readline

# 집의 개수 : n , 공유기 개수 : c
n, c = list(map(int, input().split()))
# 집의 좌표 (enter로 입력)
array = [int(input()) for i in range(n)]

array.sort() # 집 오름차순 정렬

start = 1 # 시작점 (집과 집 사이 거리 최소)
end = array[-1] - array[0] # 끝점 (집과 집 사이 거리 최대)

# 가장 인접한 두 공유기 사이의 최대거리 = mid

result = 0

while(start <= end):
  current = array[0] # 현재 집
  count = 1 # 항상 1번째 집에는 공유기를 설치. 그래야 가장 인접한 두 공유기 사이의 거리가 최대가 됨
  mid = (start + end) // 2
  for i in range(1,n):
    if array[i] - current >= mid: # 하나 더 설치해야 함.
      count += 1
      current = array[i] # i번째 인덱스에 공유기 설치
    
  if count >= c: # 공유기 개수를 넘으면
    if result < mid:
      result = mid # 가장 인접한 두 공유기 사이의 최대거리!
    start = mid + 1  # result가 mid보다 크면 mid를 늘려야하므로 start = mid + 1
  
  else: # 설치된 공유기 수가 주어진 공유기 개수(c)를 안 넘으면
    end = mid - 1 # mid가 너무 큰 것이므로 end = mid - 1
    
print(result)
