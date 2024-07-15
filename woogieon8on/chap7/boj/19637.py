import sys
input = sys.stdin.readline

n, m = map(int, input().split())
titles = [input().split() for _ in range(n)]
titles.sort(key = lambda x: int(x[1])) # 칭호를 전투력에 따라 오름차순 정렬

chars = [int(input().strip()) for _ in range(m)] # 각 캐릭터의 전투력을 정수 리스트로 생성

for char in chars:

    low = 0
    high = len(titles) - 1 # 이진 탐색 끝점: 칭호 마지막 인덱스
    result = 0 # 결과값 인덱스

    while low <= high:
        mid = (low + high)//2

        if int(titles[mid][1]) >= char: # 중간 칭호의 전투력보다 캐릭터의 전투력이 낮거나 같은 경우
            result = mid # 결과값을 중간 인덱스로 갱신
            high = mid - 1
        else:
            low = mid + 1

    print(titles[result][0]) # 캐릭터의 칭호 출력