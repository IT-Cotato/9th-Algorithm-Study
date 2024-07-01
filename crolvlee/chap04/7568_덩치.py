import sys
N = int(input())

data_list = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    data_list.append([weight, height])

for i in data_list:
    rank = 1
    for j in data_list:
        if i[0] < j[0] and i[1] < j[1]: #뒤의 사람이 덩치가 더 크면
            rank += 1
    print(rank, end= " ")
