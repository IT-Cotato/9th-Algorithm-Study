N, M = map(int, input().split())
count = 0   # 변환 횟수
is_success = 1

before_matrix = [list(map(int, input())) for _ in range(0, N)]
answer_matrix = [list(map(int, input())) for _ in range(0, N)]

# 행렬 변환 함수
def matrix_operation(i, j, arr):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            arr[x][y] = 1 - arr[x][y]

# 행렬 변환 수행
# before_matrix의 (i, j)의 위치에 있는 원소의 값이 after_matrix의 (i, j)의 위치에 있는 원소의 값과 다를 경우
for i in range(0, N - 2):
    for j in range(0, M - 2):
        if before_matrix[i][j] != answer_matrix[i][j]:
            matrix_operation(i, j, before_matrix)
            count += 1

# 검증
# 위의 과정을 통해 변환된 before_matrix와 answer_matrix가 같은지 검증
for i in range(0, N):
    for j in range(0, M):
        if before_matrix[i][j] != answer_matrix[i][j]:
            is_success = 0

# 출력
if(is_success):
    print(count)
else:
    print(-1)
