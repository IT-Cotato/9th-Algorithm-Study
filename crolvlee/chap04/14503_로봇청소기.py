N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []

cleaning_count = 0

for _ in range(N):
    data = list(map(int, input().split()))
    room.append(data)

while True:
    # 1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소
    if room[r][c] == 0:
        cleaning_count += 1
        room[r][c] = 2

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if room[r][c-1] != 0 and room[r][c+1] != 0 and room[r-1][c] != 0 and room[r+1][c] != 0:
        # 2-1. 바라보는 방향을 유지한 채 후진할 수 있다면
        if d == 0 and room[r+1][c] != 1:
            r += 1
            continue
        elif d == 1 and room[r][c-1] != 1:
            c -= 1
            continue
        elif d == 2 and room[r-1][c] != 1:
            r -= 1
            continue
        elif d == 3 and room[r][c+1] != 1:
            c += 1
            continue

        # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
        else:
            break

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if room[r][c-1] == 0 or room[r][c+1] == 0 or room[r-1][c] == 0 or room[r+1][c] == 0:
        if d == 0:
            d = 3
            if room[r][c-1] == 0:
                c -= 1
                continue
        if d == 1:
            d = 0
            if room[r-1][c] == 0:
                r -= 1
                continue
        if d == 2:
            d = 1
            if room[r][c+1] == 0:
                c += 1
                continue
        if d == 3:
            d = 2
            if room[r+1][c] == 0:
                r += 1
                continue

print(cleaning_count)