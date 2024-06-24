# 이것이 코딩테스트다 3장 큰 수의 법칙

n, m, k = map(int, input().split()) # n 배열의 크기, m 더하는 횟수, k 최대 연속 가능한 개수
data = list(map(int, input().split()))

data.sort(reverse=True) # 입력 받은 수들을 내림차순 정렬함

first = data[0] # 가장 큰 수
second = data[1] # 두 번째로 큰 수

count = int(m / (k+1)) * k
count += m % (k+1) # M이 k+1로 나누어떨어지지 않는 경우

total = count * first + (m - count) * second
print(total)