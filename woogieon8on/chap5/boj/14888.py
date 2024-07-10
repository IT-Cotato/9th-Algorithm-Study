N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

maxNum = -1e9
minNum = 1e9

def dfs(i, num, add, sub, mul, div):
    global maxNum, minNum # 최댓값, 최솟값 전역변수 선언

    if i == N: # N개의 수 모두 연산 완료
        maxNum = max(num, maxNum) # 최댓값 업데이트
        minNum = min(num, minNum) # 최솟값 업데이트
        return
    
    # 덧셈, 뺄셈, 곱셈, 나눗셈 재귀적으로 호출
    # 연산자 우선순위 무시하고 앞에서부터 연산 진행
    if add > 0: # 덧셈
        dfs(i + 1, num + nums[i], add - 1, sub, mul, div)
    if sub > 0: # 뺄셈
        dfs(i + 1, num - nums[i], add, sub - 1, mul, div)
    if mul > 0: # 곱셈
        dfs(i + 1, num * nums[i], add, sub, mul - 1, div)
    if div > 0: # 나눗셈
        dfs(i + 1, int(num / nums[i]), add, sub, mul, div - 1) # // 연산자 사용해봤는데 결과 오류남ㅜㅜ

dfs(1, nums[0], op[0], op[1], op[2], op[3])

print(maxNum)
print(minNum)