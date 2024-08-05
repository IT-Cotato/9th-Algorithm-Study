N = int(input())
student = []

for _ in range(N):
  student.append(input().split())

# [1] 감소, [2] 증가, [3] 감소, [0] 증가 순
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
  print(i[0])