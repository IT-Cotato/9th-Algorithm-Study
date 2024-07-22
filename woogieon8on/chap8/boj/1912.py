import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

for i in range(1,n) :
    x[i] = max(x[i], x[i-1] + x[i]) # 수열에서 현재 인덱스 기준으로 (현재 값)과 (이전 값 + 현재 값)을 비교하여 큰 값으로 갱신

print(max(x)) # 갱신 작업이 완료된 수열에서 최댓값 출력