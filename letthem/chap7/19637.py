import sys
input = sys.stdin.readline

# 칭호의 개수 : n, 캐릭터들의 개수 : m, 칭호의 이름과 전투력 상한값 : tag, 캐릭터의 전투력 : chars
n, m = map(int, input().split())
tag = [input().split() for _ in range(n)]
chars = [int(input().strip()) for _ in range(m)]

tag.sort(key=lambda x: int(x[1])) # 칭호의 전투력 상한값만 뽑아 오름차순 정렬

for char in chars: # 캐릭터마다 칭호 붙여줘야 함
  left = 0
  right = len(tag)
  result = 0

  while left <= right:
    mid = (left + right) // 2
    if int(tag[mid][1]) >= char: # 캐릭터의 전투력보다 mid값이 크거나 같으면
      result = mid # 전투력 상한값으로 등록
      right = mid - 1 # 상한값을 줄여본다
    else:
      left = mid + 1 # 상한값을 늘려본다
      
  print(tag[result][0]) # 칭호 이름[0] 출력