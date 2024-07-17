import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
low, high = 0, n-1
result = [liquids[low], liquids[high]] # 결과값 리스트

while low <= high:

    total = liquids[low] + liquids[high] # 용액 특성값의 합

    if total < 0: # 용액의 특성값들은 이미 오름차순 정렬
                  # 특성값의 합이 0보다 작다면 low 1 증가
        low += 1
    elif total < 0:
        high -= 1 # 합이 0보다 크다면 high 1 감소
    else:
        break # 합이 0이면 바로 결과 출력

    if abs(sum(result)) >= abs(liquids[low] + liquids[high]): # '현재 결과값의 절대값'보다 '변경된 low와 high 합의 절대값'이 작거나 같은 경우
        result = [liquids[low], liquids[high]] # 결과값 갱신

print(result[0], result[1])