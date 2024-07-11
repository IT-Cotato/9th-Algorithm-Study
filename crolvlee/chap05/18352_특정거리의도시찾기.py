import sys
input = sys.stdin.readline  # 시간초과 문제 해결하기 위해 필요

n, m, k, x = map(int, input().split())

edges = {i: [] for i in range(1, n + 1)}

for i in range(m):
    vtx1, vtx2 = map(int, input().split())
    edges[vtx1].append(vtx2)

# BFS 초기화
distance = [-1] * (n + 1)   # 0번 정점은 없으므로 비워둠. 나머지 1~n번 정점
distance[x] = 0
queue = [x]

# BFS 실행
head = 0    # queue의 첫 번쨰 요소를 가리킬 인덱스
while head < len(queue):
    current = queue[head]
    head += 1
    for neighbor in edges[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if found == False:
    print(-1)

