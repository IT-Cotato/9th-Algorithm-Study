import sys
input = sys.stdin.readline

n = int(input()) # 전체 용액의 수
liq = list(map(int, input().split())) # 용액의 특성값

min = float("INF") # 절댓값이 가장 작은 (=0에 가까운) 값
answer = [float('INF'), float('INF')]

left = 0
right = n - 1

while left < right:
  if abs(liq[left] + liq[right]) < min: # 더한 것의 절댓값이 현재 min값보다 작으면 업데이트
    min = abs(liq[left] + liq[right])
    answer = [liq[left], liq[right]]
  
  if liq[left] + liq[right] < 0:
    left += 1 # index 늘리기
  else:
    right -= 1 # index 줄이기

print(*answer)