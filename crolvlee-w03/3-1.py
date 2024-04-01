# 큰 수의 법칙

n, m, k = map(int, input().split())
data_list = list(map(int, input().split()))

data_list.sort()

x = data_list[-1]   # 가장 큰 값
y = data_list[-2]   # 두번째로 큰 값

result = (k * int(m / k)) * x + (m % k) * y

print(result)