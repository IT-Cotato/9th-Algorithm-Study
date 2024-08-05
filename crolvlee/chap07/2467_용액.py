import sys
input = sys.stdin.read

# 입력받음
data = input().split()
n = int(data[0])
liquids = list(map(int, data[1:]))

# 최소값 초기화
closest_value = float('inf')
answer_left = 0
answer_right = 0

# 이진 탐색을 통해 가장 가까운 두 용액 찾기
for i in range(n - 1):
    left, right = i + 1, n - 1
    while left <= right:
        mid = (left + right) // 2
        current_sum = liquids[i] + liquids[mid]

        # 현재 합의 절대값이 이전 최소값보다 작으면 정보 갱신
        if abs(current_sum) < closest_value:
            closest_value = abs(current_sum)
            answer_left = i
            answer_right = mid

        if current_sum < 0:
            left = mid + 1      # 현재 범위보다 큰 곳을 탐색
        else:
            right = mid - 1     # 현재 범위보다 작은 곳을 탐색


if liquids[answer_left] > liquids[answer_right]:
    answer_left, answer_right = answer_right, answer_left

print(liquids[answer_left], liquids[answer_right])
