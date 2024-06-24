n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 이진 탐색을 위해 시작점과 끝점(가장 높이가 높은 나무) 지정
start = 0
end = max(trees)

result = 0
# 이진 탐색
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid: # (현재 나무 높이 - mid)값 만큼 나무 절단
            total += tree - mid
    
    if total < m: # 절단한 나무 길이의 합이 가져가려는 나무의 길이보다 짧은 경우
        end = mid - 1 # 절단 높이를 내려 절단한 나무 길이의 합 증가
    else: # 절단한 나무 길이의 합이 충분한 경우
        result = mid
        start = mid + 1 # 절단 높이를 올려 절단한 나무 길이의 합 감소

print(result)