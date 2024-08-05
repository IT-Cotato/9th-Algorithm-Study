from collections import deque
import sys
input = sys.stdin.readline

# 수빈 위치, 동생 위치
n, k = map(int,input().split())

MAX_SIZE = 100001

que = deque()
que.append(n)
visited = [-1] * MAX_SIZE # 방문 시간을 -1로 초기화
visited[n] = 0 # 수빈이의 시작 위치는 이미 방문 -> 방문 시간 0으로.
cnt = 0 # 가장 빠른 시간으로 동생을 찾는 '방법'의 수

while que:
    # 현재 위치
    current = que.popleft()

    # 동생에게 도착한 경우
    if current == k:
        cnt += 1 # 방법 하나 추가
    
    # 동생에게 도착 안 한 경우 이동. (순간이동, 앞으로 이동, 뒤로 이동)
    for next in [current * 2, current + 1, current - 1]:
        if 0 <= next < MAX_SIZE: # 다음 위치가 범위 내일 때
          # 방문한 적 없었거나, 방문한 적 있지만 현재 노드에서 가는 경우보다 더 오래걸렸다면 현재 노드에서 가는 방법이 더 빠르므로 업데이트
            if visited[next] == -1 or visited[next] >= visited[current] + 1:
                visited[next] = visited[current] + 1 # 방문시간 +1 해줌
                que.append(next) # q에 넣음

print(visited[k]) # k까지 걸린 시간
print(cnt) # k까지 빠르게 가는 개수