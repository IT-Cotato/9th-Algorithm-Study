n, k = map(int, input().split())

medals = []
for i in range(n):
	medals.append(list(map(int, input().split())))

medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True) # 내림차순. 금, 은, 동 많은 순서로 정렬

ranking = 1
same = 0


for i in range(n):
    if i != 0:
      if medals[i-1][1:] == medals[i][1:]: # 메달 모두 같으면
        same += 1 # 같은 등수 count
      else: # 메달 개수 다르면
        if same != 0: # 같은 등수 있으면
          ranking += same # ranking에 same 더해주기
          same = 0 # same 다시 0으로 초기화
        ranking += 1 # 같은 등수 없으면 등수 + 1
    if medals[i][0] == k:
      print(ranking)
      break