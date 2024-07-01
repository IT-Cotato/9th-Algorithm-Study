import sys
In=sys.stdin.readline

n=int(In())
people=[tuple(map(int,In().split())) for _ in range(n)]

for i in people:
    rank=1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]: rank+=1
    print(rank, end=' ')