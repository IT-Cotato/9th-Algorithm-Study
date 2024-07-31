import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

result = 0  # 배정된 예산들 중 최댓값
start, end = 1, max(budgets) # 이진 탐색 끝점: 가장 큰 예산 요청

# 이진 탐색
while start <= end:

    mid = (start + end) // 2
    total = 0  # 예산의 합

    for budget in budgets:
        if budget > mid: # 예산 요청이 중간값보다 큰 경우
            total += mid # 중간값을 더함
        else: 
            total += budget # 예산 요청이 중간값보다 작기 때문에 예산 요청을 더함

    if total <= m:  # 예산의 합이 총 예산보다 작거나 같은 경우
        result = mid # 결과값을 중간값으로 갱신
        start = mid + 1
    else:  
        end = mid - 1

print(result)