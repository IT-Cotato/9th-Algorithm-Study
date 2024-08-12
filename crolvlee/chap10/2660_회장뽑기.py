import sys
input = sys.stdin.readline
INF = float('inf')

# 입력받음
n = int(input())

# 그래프 초기화
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

# 연결된 노드들을 그래프에 담음
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1
    
# 플로이드 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
# 각 회원의 점수 계산
scores = []
for i in range(1, n+1):
    max_distance = max(dist[i][1:])
    scores.append((max_distance, i))
    
min_score = min(scores)[0]
candidates = []
for score, member in scores:
    if score == min_score:
        candidates.append(member)

# 후보의 회원번호를 오름차순으로 정렬
candidates.sort()

print(min_score, len(candidates))
for candidate in candidates:
    print(candidate, end=' ')