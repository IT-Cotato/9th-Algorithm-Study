N = int(input())
spot = list(map(int, input().split())) # N개

spot.sort()

print(spot[(N-1) // 2]) # 중간값