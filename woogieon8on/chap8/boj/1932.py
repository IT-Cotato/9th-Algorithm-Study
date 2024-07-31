n = int(input())

tree = []
for _ in range(n):
    tree.append(list(map(int, input().split())))

for i in range(1, n): # 첫 번째 행 제외
    for j in range(len(tree[i])):
        if j == 0: # 첫 번째 열의 경우 이전 행의 첫 번째 열 선택
            tree[i][j] = tree[i][j] + tree[i-1][j]
        elif j == len(tree[i]) - 1: # 마지막 열의 경우 이전 행의 마지막 열 선택
            tree[i][j] = tree[i][j] + tree[i-1][j-1]
        else: # 나머지는 이전 행의 같은 열, (자신의 열 - 1)에 해당하는 값 중에서 최대값 선택
            tree[i][j] = tree[i][j] + max(tree[i-1][j-1], tree[i-1][j])

print(max(tree[n-1])) # 마지막 행에서 최대값 출력