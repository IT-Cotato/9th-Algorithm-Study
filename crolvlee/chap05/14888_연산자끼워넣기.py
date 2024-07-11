import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

def dfs(depth, total, add, sub, mul, div):
    global max_num, min_num

    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    
    if add > 0:
        dfs(depth + 1, total + A[depth], add - 1, sub, mul, div)
    if sub > 0:
        dfs(depth + 1, total - A[depth], add, sub - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, total * A[depth], add, sub, mul - 1, div)
    if div > 0:
        dfs(depth + 1, int(total / A[depth]), add, sub, mul, div - 1)

dfs(1, A[0], operator[0], operator[1], operator[2], operator[3])
print(max_num)
print(min_num)
