import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
members = [[] for _ in range(n+1)] # 회원별 친구 리스트
count = [0] * (n+1)

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1: # 마지막 줄
        break
    else:
        members[a].append(b)
        members[b].append(a)

def bfs(v):
    queue = deque()
    queue.append([v, 0]) # 회원 번호, 현재 깊이 큐에 추가
    visited[v] = True

    while queue:
        x, y = queue.popleft()

        for i in members[x]: # 현재 회원과 친구 관계인 모든 회원들
            if not visited[i]: # 방문하지 않은 경우
                visited[i] = True
                queue.append([i, y+1]) # 깊이를 1 증가시켜 큐에 추가

    count[v] = y # bfs 종료 후 해당 회원의 최대 깊이를 점수로 저장

for i in range(1, n+1):
    visited = [False] * (n+1)
    bfs(i) # 각 회원에 대해 bfs 수행

count.pop(0) # 회원번호 0 제거
answer = [] # 회장 후보 리스트

for i in range(n): # 최소 점수 가진 회원 찾기
    if count[i] == min(count):
        answer.append(i+1)

print(min(count), count.count(min(count))) # 최소 점수와 그 점수를 가진 회원 수 출력
print(*answer) # 회장 후보 회원 번호 출력