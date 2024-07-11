import sys
from collections import deque
input = sys.stdin.readline

N, K= map(int, input().split())
queue = deque()
queue.append(N)

way = [0]*100001 # 각 위치까지의 시간 배열
cnt, result = 0,0

while queue:
    a =  queue.popleft()
    temp = way[a]

    if a == K: # 수빈이와 동생이 만난 경우
        result = temp # temp(=way[a]) 값이 최소 시간
        cnt += 1 # 최소 시간으로 동생을 찾는 방법 개수 + 1
        continue
    
    for i in [a-1, a+1, a*2]: # 수빈이가 걷거나 순간이동 해서 도착하는 다음 위치에 대하여
        if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a] + 1): # 범위 안에 있으면서, 아직 방문하지 않았거나 해당 위치까지의 시간이 동일한 경우
            way[i] = way[a] + 1 # 해당 위치까지의 시간을 1 증가시킨 후 큐에 추가
            queue.append(i) 

print(result)
print(cnt)