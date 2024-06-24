n, k = map(int, input().split())

num = 0

while (n >= k): # n이 k보다 같거나 클 때
  while(n % k != 0): # 나머지가 있으면
    n = n - 1 # 1만큼 빼기
    num += 1
  n = n // k # 나머지가 없으면 k로 나누기
  num += 1

while n > 1: # n이 1보다 클 때
  n = n - 1 # 1만큼 빼기
  num += 1
  
print(num)