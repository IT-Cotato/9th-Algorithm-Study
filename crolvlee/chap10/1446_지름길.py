N, D = map(int, input().split())
shortcut = {}
# shortcut = {(0, 50): 10, (50, 100): 10, (100, 151): 10, ....}

for _ in range(N):
    start, end, length = map(int, input().split())
    
    # shortcut에 지름길 넣기
    # 더 오래 걸리는 지름길은 shortcut에 추가 안 함
    if end > D:
        continue

    if end - start < length:
        continue

    if (start, end) in shortcut:
        if shortcut[(start, end)] > length:
            shortcut[(start, end)] = length
    else:
        shortcut[(start, end)] = length

# 최소 거리를 계산하기 위한 dp배열 초기화
dp = [float('inf')] * (D + 1)
dp[0] = 0

# 직진 경로와 지름길을 고려하여 dp 배열 업데이트
for i in range(1, D + 1):
    # 직진 경로를 고려
    dp[i] = min(dp[i], dp[i - 1]+1)

    # 지름길이 있는 경우를 고려
    for (start, end), length in shortcut.items():
        if i == end and start < i:
            dp[i] = min(dp[i], dp[start] + length)

print(dp[D])