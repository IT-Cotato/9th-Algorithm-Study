import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

for i in range(1, n):
  m[i] = max(m[i], m[i] + m[i-1]) # 더한 것과 자신을 비교하여 더 큰 것으로 업데이트
    
print(max(m))