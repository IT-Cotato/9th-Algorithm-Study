row, col = map(int, input().split())

a = [list(map(int, input()))for _ in range(row)]
b = [list(map(int, input()))for _ in range(row)]

def flip(x,y):
    for i in range(3):
        for j in range(3):
            a[x+i][y+j] = 1 - a[x+i][y+j]

answer = 0

for i in range(row-2):
    for j in range(col-2):
        if a[i][j] != b[i][j]:
            flip(i,j)
            answer += 1
        if a == b:
            break
    if a==b:
        break

if a == b:
    print(answer)
else:
    print(-1)