n, m = map(int, input().split())

vaccum_move_map = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
vaccum_move_map[x][y] = 1

vaccum_map = []
for i in range(n):
    vaccum_map.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if vaccum_move_map[nx][ny] == 0 and vaccum_map == 0:
        vaccum_move_map[nx][ny] = 1
        cnt += 1
        x, y = nx, ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if vaccum_map[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(cnt)