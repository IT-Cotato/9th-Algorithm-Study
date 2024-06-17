N, M = map(int, input().split())

data = []
temp = [[0] * M for _ in range(N)]  # 바이러스의 퍼짐을 나타낼 임시 지도

for _ in range(N):
    data.append(list(map(int, input().split())))

# 순서대로 서남동북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 안전 영역의 크기
result = 0

# DFS로 바이러스 퍼지게 하는 함수 [위치 (x, y)에 있는 바이러스를 퍼지게 하기]
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 바이러스가 퍼질 수 있는 경우
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 이용하여 울타리를 설치하기
def main_dfs(count):
    global result

    # 울타리가 3개인 경우
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j] # 임시 지도에 현재 지도를 복사

        # 각 바이러스의 위치에서 전파 진행
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    
    # 빈 공간에 울타리 설치
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                main_dfs(count) # 다음 울타리 설치를 위해 재귀 호출
                data[i][j] = 0  # 설치했던 울타리를 다시 제거
                count -= 1


main_dfs(0)
print(result)
