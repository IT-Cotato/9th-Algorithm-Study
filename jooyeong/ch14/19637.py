import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

for i in range(N):
    name, max_score = input().split()
    max_score = int(max_score)
    
    arr.append((max_score, name))

for _ in range(M):
    score = int(input())

    start, end = 0, len(arr)

    while start <= end:
        mid = (start + end) // 2

        if score <= arr[mid][0]:
            end = mid - 1
        else:
            start = mid + 1

    print(arr[start][1])