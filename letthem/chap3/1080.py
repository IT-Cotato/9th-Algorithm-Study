from sys import stdin

n, m = map(int, stdin.readline().split())
A = [list(map(int,stdin.readline().rstrip())) for _ in range(n)] # 원래 행렬
B = [list(map(int,stdin.readline().rstrip())) for _ in range(n)] # toggle 했을 때 원하는 결과 행렬


# 행렬 변환 함수. 1이면 0, 0이면 1
def toggle(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            A[i][j] ^= 1 # 1과 XOR(다르면 1) 연산. 0이면 0^1=>1. 1이면 1^1=>0.

cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]: # 맨 왼쪽 위 원소가 B와 다르다면 뒤집자. 같으면 뒤집지 말자 => 그리디 알고리즘
            toggle(i,j) # toggle 해보기!
            cnt += 1

print(cnt if A == B else -1)