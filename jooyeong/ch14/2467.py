import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
value = sys.maxsize
answer = []
while left < right:
    if abs(arr[left]+arr[right]) <= value:
        answer = [arr[left], arr[right]]
        value = abs(arr[left]+arr[right])
    if arr[left]+arr[right] < 0:
        left += 1
    elif arr[left]+arr[right] > 0:
        right -= 1
    else:
        break

print(*answer)