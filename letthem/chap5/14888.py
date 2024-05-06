N = int(input())
num = list(map(int, input().split())) # N개
op = list(map(int, input().split())) # N - 1개

maxNum = -1e9
minNum = 1e9

def dfs(index, total, add, sub, mul, div):
    global maxNum, minNum
    if index == N: # index가 N일 때
        maxNum = max(total, maxNum) # 최댓값
        minNum = min(total, minNum) # 최솟값
        return

    # 재귀 함수
    if add > 0:
        dfs(index + 1, total + num[index], add - 1, sub, mul, div)
    if sub > 0:
        dfs(index + 1, total - num[index], add, sub - 1, mul, div)
    if mul > 0:
        dfs(index + 1, total * num[index], add, sub, mul - 1, div)
    if div > 0:
        dfs(index + 1, int(total / num[index]), add, sub, mul, div - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])

print(maxNum)
print(minNum)