n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

sum = 0

# m이 0이 될 때까지 가장 큰 걸 k번 더하고 두 번째로 큰 걸 1번 더하고 가장 큰 걸 k번 더하고 두 번째로 큰 걸 1번 더하고 반복,,

while True:
  for i in range(k): # 가장 큰 수 k번 더하기
    if m == 0: # m이 0이면 탈출
      break
    sum += max(num_list) # 가장 큰 수 더하기
    m -= 1 # m 하나 빼기
  if m == 0: # m이 0이면 탈출
    break
  sum += sorted(num_list, reverse=True)[1] # 두 번째로 큰 수 더하기
  m -= 1 # m 하나 빼기

print(sum)