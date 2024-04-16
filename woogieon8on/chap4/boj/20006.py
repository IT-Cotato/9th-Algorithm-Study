p, m = map(int,input().split())

rooms = []

for i in range(p):
    l, n = input().split()

    # 첫 플레이어 방 만들기
    if not rooms:
        rooms.append([[int(l),n]])
        continue
	
    enter = False
    for room in rooms:
        # 입장 가능한 방이 있으면 입장
        if len(room) < m and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l),n])
            enter = True
            break
	# 입장 가능한 방이 없는 경우 방 만들기
    if not enter:
        rooms.append([[int(l),n]])

for room in rooms :
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    for l, n in room:
        print(l, n)