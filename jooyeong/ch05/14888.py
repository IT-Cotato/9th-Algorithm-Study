# DFS로 풀이

n = int(input()) # 개수
num = list(map(int, input().split())) # 수열을 리스트로 저장
plus, minus, multi, div = map(int, input().split()) # 연산자별 개수

maximum = -1e9
minimum = 1e9

def dfs(i, temp):
    global maximum, minimum, plus, minus, multi, div

    if i == n-1 : # 모든 노드를 탐색했을 경우
        maximum = max(maximum, temp)
        minimum = min(minimum, temp)

    # 각 연산자가 있는지 확인
    # -> 해당 연산자 개수 -1
    # -> 해당 연산 계산 & i+1하며 dfs 재귀 호출
    # -> 연산자 개수 다시 +1
    # (연산자 개수를 +1 하지 않으면 처음 계산한 값이 그대로 최댓값, 최솟값으로 출력되며 실행이 종료됨.)

    if plus > 0 :
        plus -= 1 # 1 1 1 1
        dfs(i+1, temp + num[i+1])
        plus += 1

    if minus > 0 :
        minus -= 1
        dfs(i+1, temp - num[i+1])
        minus += 1

    if multi > 0 :
        multi -= 1
        dfs(i+1, temp * num[i+1])
        multi += 1

    if div > 0 :
        div -= 1
        dfs(i+1, int(temp / num[i+1]))
        div += 1

dfs(0, num[0])

print(maximum)
print(minimum)