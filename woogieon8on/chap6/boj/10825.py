N = int(input())

students = []
for _ in range(N):
    students.append(input().split())

# 기본 형식: sort(key = lamda x: (정렬 대상))
# 리스트의 각 원소가 튜퓰 형태로 존재할 때, 우선순위를 정하여 정렬 가능
# 오름차순: 생략 ex) int(x[2])
# 내림차순: 변수 앞에 - 붙이기 ex) -int(x[1])
students.sort(key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in students:
    print(student[0])