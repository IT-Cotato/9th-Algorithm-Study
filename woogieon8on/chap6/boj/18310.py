N = int(input())
house = list(map(int, input().split()))

# 모든 집까지의 거리의 총합
# : 안테나를 모든 집들 중 중간에 위치한 집에 설치한 경우 최소
house.sort()
antenna = house[int((N - 1) / 2)] # 안테나를 설치할 수 있는 위치 값으로 여러 개의 값이 도출될 경우 가장 작은 값 출력

print(antenna)