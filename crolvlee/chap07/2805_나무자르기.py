N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

cutter_h = 0  # 절단기 높이

while start <= end:
    cut_sum = 0  # 가져갈 나무의 길이

    mid = (start + end) // 2  # 절단기의 높이

    for i in tree:
        if i > mid:  # 절단기의 높이보다 주어진 나무가 긴 경우
            cut_sum += i - mid

    # 이진 탐색
    if cut_sum < M:
        end = mid - 1
    else:
        cutter_h = mid
        start = mid + 1

print(cutter_h)
