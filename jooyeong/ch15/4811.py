def solve(w, h):
    if dp[w][h] != -1:
        return dp[w][h]
    dp[w][h] = 0

    if w == 0:
        dp[w][h] = 1
        return dp[w][h]
    if h < 0:
        return 0

    dp[w][h] = solve(w - 1, h + 1) + solve(w, h - 1)
    return dp[w][h]


dp = [[-1] * 31 for _ in range(31)]

while True:
    N = int(input())

    if N == 0:
        break

    print(solve(N - 1, 1))