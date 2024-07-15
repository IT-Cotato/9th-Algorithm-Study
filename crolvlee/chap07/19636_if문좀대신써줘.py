import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_list = []
power_list = []

# 정보 입력받기
for _ in range(N):
    name, power = input().split()
    power = int(power)

    if not power_list or power != power_list[-1]:     # power_list에 저장되지 않은 경우에만 넣음
        power_list.append(power)
        name_list.append(name)

result = []

for _ in range(M):
    character_power = int(input())
    low = 0
    high = len(power_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if character_power <= power_list[mid]:
            high = mid - 1  # 현재 범위보다 작은 곳을 탐색
        else:
            low = mid + 1   # 현재 범위보다 큰 곳을 탐색
    result.append(name_list[low])



for r in result:
    print(r)

