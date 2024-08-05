import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]
count = 0

# 3x3 크기의 부분 행렬에 있는 모든 원소 뒤집는 메소드
def convert(x, y, a):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j] # 0 -> 1, 1 -> 0

# convert 메소드 유의하여 범위 설정
for i in range(n-2):
    for j in range(m-2):
        count += 1
        convert(i, j, a)

if a != b: # A를 B로 바꿀 수 없다면 -1 출력
    print(-1)
else:
    print(count)