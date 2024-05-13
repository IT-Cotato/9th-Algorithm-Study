n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# 블루레이 크기를 이진탐색의 초기 범위로 지정
start = max(lectures) # 모든 강의를 각각 블루레이로 녹화할 경우 블루레이의 크기 최소 -> 길이가 가장 긴 강의의 길이
end = sum(lectures) # 모든 강의를 한 번에 블루레이로 녹화할 경우 블루레이의 크기 최대 -> 모든 강의 길이의 합

result = 0
# 이진 탐색
while(start <= end):
    total = 0
    bluray = 1
    mid = (start + end) // 2
    for lec in lectures:
        if total + lec > mid: # 강의 길이의 총 합이 블루레이 크기보다 큰 경우
            bluray += 1 # 블루레이 개수 1 증가
            total = 0 # 강의 길의의 총 합 초기화
        total += lec

    if bluray > m: # 블루레이 개수가 원하는 개수보다 많은 경우
        start = mid + 1 # 블루레이 개수 줄이기 위해 블루레이 크기 증가
    else:
        result = mid
        end = mid - 1 # 블루레이 개수 늘리기 위해 블루레이 크기 감소

print(result)