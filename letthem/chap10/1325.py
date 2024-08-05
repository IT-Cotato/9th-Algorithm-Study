import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())  # n : 컴퓨터의 개수, m : 신뢰관계의 개수
com = [[] for _ in range(n + 1)]  # 인접 리스트 초기화

# 신뢰 관계 입력
for _ in range(m):
  a, b = map(int, input().split())
  com[b].append(a)  # a가 b를 신뢰 => b를 해킹하면 a를 해킹할 수 있음 => b에 a를 추가

# 시작 컴퓨터 i에서 해킹할 수 있는 컴퓨터 수를 계산하는 함수
def bfs(i):
  q = deque([i])
  visit = [0] * (n + 1)  # visit : 각 컴퓨터의 방문 여부 체크
  visit[i] = 1 # 자기 자신은 1
  cnt = 1  # 해킹할 수 있는 컴퓨터의 수
  while q:
    current = q.popleft()
    for neighbor in com[current]:  # 그 컴퓨터에서 또 해킹할 수 있는 컴퓨터 꺼내기
      if not visit[neighbor]:
        q.append(neighbor)
        visit[neighbor] = 1
        cnt += 1
  return cnt

max_cnt = 0  # 가장 큰 cnt 초기화
ret = []  # return 리스트 초기화

for i in range(1, n + 1):  # 모든 컴퓨터마다 다 bfs해서 탐색
  cnt = bfs(i)
  if cnt > max_cnt:  # 가장 큰 cnt (가장 많이 해킹할 수 있는 컴퓨터)
    max_cnt = cnt
    ret = [i]  # return 리스트 초기화 후 현재 컴퓨터 추가
  elif cnt == max_cnt:
    ret.append(i)  # 중복도 가능하게

print(*ret)
