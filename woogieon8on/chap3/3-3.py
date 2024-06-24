n, m = map(int, input().split())

result = 0
for i in range(n):
    num = list(map(int, input().split()))
    min_value = min(num) # 행에서 가장 작은 수
    result = max(result, min_value) # 가장 작은 수 중에서 가장 큰 수

print(result)