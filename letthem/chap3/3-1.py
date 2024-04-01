n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

sum = 0

# m이 0이 될 때까지 가장 큰 걸 k번 더하고 두 번째로 큰 걸 1번 더하고 가장 큰 걸 k번 더하고 두 번째로 큰 걸 1번 더하고 반복,,

while True:
  for i in range(k):
    if m == 0:
      break
    sum += max(num_list)
    m -= 1
  if m == 0:
    break
  sum += sorted(num_list, reverse=True)[1]
  m -= 1

print(sum)