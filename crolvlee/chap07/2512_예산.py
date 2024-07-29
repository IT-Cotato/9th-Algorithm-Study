import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
<<<<<<< HEAD
M = int(input())    # 빌려줄 수 있는 총액
=======
M = int(input())    # 예산 상한선
>>>>>>> upstream/main

start = 0
end = max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2   # 기준 상한 금액

    # 상한 금액이 mid일 때, 받는 요청 금액의 합 total 구하기
    total = 0
    for l in lst:
<<<<<<< HEAD
        if l >= mid:        # 상한금액 mid를 넘으면
            total += mid
        else:               # 상한 금액 mid를 넘지 않으면
=======
        if l >= mid:
            total += mid
        else:
>>>>>>> upstream/main
            total += l

    # total이 주어진 금액을 초과하는지 여부에 따라 포인트 재설정
    if total <= M:
        answer = mid        # 현재 mid값이 가능하긴 함
<<<<<<< HEAD
        start = mid + 1     # 현재 mid값보다는 큰 범위를 탐색
    else:
        end = mid - 1       # 현재 mid값보다는 작은 범위를 탐색
=======
        start = mid + 1     # 현재 mid값보다는 작은 범위를 탐색
    else:
        end = mid - 1       # 현재 mid값보다는 큰 범위를 탐색
>>>>>>> upstream/main

print(answer)