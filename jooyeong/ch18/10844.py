n = int(input())
list = [0]*10
for i in range(1, 10):
  list[i] = 1
for i in range(2, n+1):
  temp = [0]*10
  for j in range(10):
      if j-1 >= 0:
          temp[j-1] += list[j]
      if j+1 <= 9:
          temp[j+1] += list[j]
  list = temp.copy()
print(sum(list)%1000000000)