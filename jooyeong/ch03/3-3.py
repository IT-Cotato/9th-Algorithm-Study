# 이것이 코딩테스트다 3장 숫자 카드 게임

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 한 줄씩 입력받음
    min_data = min(data)
    # 입력받은 data 중 최솟값을 찾음
    result = max(result, min_data)
    # 기존에 저장되어있던 result와 min_data를 비교해서 더 큰 값을 저장함
    # for문이 반복되며 result값이 업데이트되므로, 반복이 종료되는 시점에는 result에 각 행별 최솟값 중 가장 큰 값이 저장되어 있을 것임

print(result)

# min_value = 10001
# for a in data:
#   min_value = min(min_value, a)