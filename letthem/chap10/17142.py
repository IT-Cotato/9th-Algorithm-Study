from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 크기가 n x m 인 직사각형
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 벽을 세울 수 있는 후보 위치 저장
empty_spaces = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]


def bfs():
    queue = deque()
    # 원래의 graph는 유지시킴 (원래 graph 갖다 붙여넣기). 원본 그래프를 유지하면서 바이러스 확산 시뮬레이션을 진행할 수 있음
    tmp_graph = [row[:] for row in graph] # 깊은 복사를 피하기 위해 슬라이싱 사용

    # 바이러스 초기 위치를 큐에 넣는다
    # tmp_graph에서 바이러스가 있는 위치(값이 2인 부분)를 찾아 큐에 추가한다
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    # 탐색 시작(bfs로 바이러스 퍼뜨리기)
    while queue: # 큐가 빌 때까지 반복하며 상하좌우로 이동하여 바이러스를 퍼트림
        x, y = queue.popleft() # 현재 위치 꺼내오기

        # 상하좌우라 range(4). 현재위치에서 상하좌우로 이동 가능한지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and tmp_graph[nx][ny] == 0: # 범위 확인 및 감염 가능 여부 확인. 0이면 감염(2) 가능
                tmp_graph[nx][ny] = 2
                # 큐에 추가
                queue.append((nx, ny))

    # 바이러스가 모두 퍼진 후 안전 영역(값이 0인 부분)을 세어 result에 최대값을 갱신.
    count = sum(row.count(0) for row in tmp_graph)
    return count

def make_wall(count, start):
    # 벽 3개가 세워지면 바이러스 퍼트리기
    global result
    if count == 3: # 벽을 세운 후 안전 영역이 확정되었을 때
        result = max(result, bfs()) # 안전 영역 개수 세기 위해 bfs 사용
        return # 종료

    for idx in range(start, len(empty_spaces)): # 빈 공간이라면 벽 세우기 가능
        i, j = empty_spaces[idx]
        graph[i][j] = 1 # 벽을 세우고
        make_wall(count + 1, idx + 1) # 재귀: 다시 두 번째 벽 세우러 간다
        graph[i][j] = 0 # 다시 벽을 허무는 과정 (백트래킹) - 3개의 벽을 세울 수 있는 모든 경우의 수를 다 볼려고 허무는 거임,,


result = 0 # 최대 안전 영역 크기 초기값 0
make_wall(0, 0) # count와 start는 0으로 초기화하고 벽 세우기 시작

print(result) # 최대 안전 영역 크기 출력