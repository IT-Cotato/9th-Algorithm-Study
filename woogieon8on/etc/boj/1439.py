import sys
input = sys.stdin.readline

s = input().strip()
cnt = 0 # 행동 횟수

for i in range(len(s)-1):
    if s[i] != s[i+1]: # 현재 문자와 다음 문자가 다른 경우 -> 뒤집기
        cnt += 1 # 행동 횟수 증가

print((cnt+1)//2) # 뒤집는 횟수 절반으로 줄여 행동 최소 횟수 도출 가능