from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
computer = [[] for _ in range(n+1)] # 각 컴퓨터가 해킹할 수 있는 컴퓨터 리스트

for _ in range(m):
    a, b = map(int,input().split())
    computer[b].append(a) # A가 B를 신뢰함 -> B를 해킹하면 A도 해킹 가능

def bfs(i):
    visited = [0] * (n + 1)
    queue = deque([i])
    visited[i] = 1
    cnt = 1 # 해킹할 수 있는 컴퓨터 수 (자기 자신 포함)

    while queue:
        x = queue.popleft()

        for nx in computer[x]: # 해당 컴퓨터와 신뢰 관계에 있는 모든 컴퓨터
            if not visited[nx]: # 방문하지 않은 경우
                queue.append(nx) # 큐에 추가
                visited[nx] = 1 # 방문 처리
                cnt += 1 # 해킹할 수 있는 컴퓨터 수 증가

    return cnt

answer = [] # 해킹할 수 있는 컴퓨터 수가 최대인 컴퓨터 리스트
max_hack = 0 # 최대 해킹 수

for i in range(1, n+1):
    result = bfs(i)
    if max_hack < result: # 최대 해킹 수가 더 높은 경우 갱신
        max_hack = result
        answer.clear() # 기존 답 리스트 초기화
        answer.append(i) # 리스트에 추가
    elif max_hack == result: # 최대 해킹 수가 동일한 경우
        answer.append(i) # 기존 답 리스트 초기화 없이 리스트에 추가

print(*answer)