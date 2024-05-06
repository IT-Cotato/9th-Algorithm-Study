N = int(input())

result = []

for _ in range(N):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)

    result.append([name, kor, eng, math])

# 정렬
result.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력
for r in result:
    print(r[0]) 