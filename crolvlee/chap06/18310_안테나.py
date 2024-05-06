N = int(input())

pos = list(map(int, input().split()))
pos.sort()

print(pos)

if N % 2 == 0:  # N이 짝수일 경우
    print(pos[int(N/2) - 1])
else:            # N이 홀수일 경우
    print(pos[int((N+1)/2) - 1])