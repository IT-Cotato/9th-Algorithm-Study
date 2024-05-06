p, m = map(int, input().split())

players = []

for i in range(p):
    l, n = input().split()
    players.append([int(l), n])

rooms = []

for l, n in players:
    flag = False # 방에 players 배치했는지 여부
    for i in range(len(rooms)): # 방 수 만큼 반복
        if len(rooms[i][1]) == m: # player 수 초과하면 넘어가기 - [i][1]: id(n)
            continue
        
        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= l <= rooms[i][0] + 10: # [i][0]: level
            flag = True
            rooms[i][1].append([l, n])
            break
            
    # 대기방에 들어 갈 수 없으면 새로운 방 생성
    if not flag:
        rooms.append([l, [[l, n]]])

# 방이 생성된 시간 순서로 출력
for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(m):
            print(*tmp_ids[j])
    else:
        print('Waiting!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(len(tmp_ids)):
            print(*tmp_ids[j])