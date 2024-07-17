import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2
    curr = 0
    for i in arr:
        if i >= mid:
            curr += mid
        else:
            curr += i
    if curr <= m:
        start = mid + 1
    else:  
        end = mid - 1

print(end)