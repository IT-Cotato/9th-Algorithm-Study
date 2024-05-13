n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

# 공유기 설치 간격을 이진탐색의 초기 범위로 지정
start = 1
end = houses[n-1] - houses[0]

result = 0
# 이진 탐색
while(start <= end):
    router = 1
    lastRouter = houses[0] # 마지막으로 공유기를 설치한 집
    mid = (start + end) // 2
    for house in houses:
        if house - lastRouter >= mid: # 마지막으로 공유기를 설치한 집과의 거리가 공유기 설치 간격보다 크거나 같은 경우
            router += 1 # 해당 집에 공유기 설치
            lastRouter = house

    if router < c: # 공유기의 총 개수가 설치하고자 하는 공유기의 개수보다 적은 경우
        end = mid - 1 # 공유기 설치 간격 감소
    else:
        result = mid
        start = mid + 1 # 공유기 설치 간격 증가

print(result)