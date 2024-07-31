def solve(w, h):
    if dp[w][h] != -1: # 이미 계산한 거일 경우 그대로 리턴함
        return dp[w][h]
    dp[w][h] = 0
    # dp[w][h] : W가 w개 있고 H가 h개 있을 경우 만들 수 있는 문자열의 개수

    if w == 0: # w이 0개일 경우, 즉 h만 남았을 경우 남은 h를 모두 사용해서 만드는 문자 하나의 경우만 존재함
        dp[w][h] = 1
        return dp[w][h]
    if h < 0: # h가 0 미만인 경우는 없음. 0 리턴
        return 0

    # 총 문자열의 개수 = W를 사용한 경우 + H를 사용한 경우
    dp[w][h] = solve(w - 1, h + 1) + solve(w, h - 1)
    return dp[w][h]


dp = [[-1] * 31 for _ in range(31)]

while True:
    N = int(input())
    # 각 테스트 케이스를 입력받음

    if N == 0:
        break
    # 입력값이 0이면 마지막 줄이므로 입력 받는 것 종료

    print(solve(N - 1, 1))
    # 각 테스트 케이스에 대한 결과값 출력
    # N : 알약의 개수
    # 문자열의 첫 번째 문자는 무조건 W가 오게 됨 (초기 상태에는 반 조각이 없기 때문)
    # 첫째 날에 무조건 약 하나를 꺼내서 반만 먹으므로 W의 개수는 N-1, h의 개수는 첫째 날 먹고 남은 반 개가 있으므로 1