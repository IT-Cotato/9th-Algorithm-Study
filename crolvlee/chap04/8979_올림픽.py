n, k = map(int, input().split())

data_list = []

# data_list에 data 모두 넣기
for i in range(n):
    data = []
    country, gold, silver, bronze = map(int, input().split())
    data.append(country)
    data.append(gold)
    data.append(silver)
    data.append(bronze)
    
    data_list.append(data)
    
data_list_sorted = sorted(data_list, key=lambda x : (-x[1], -x[2], -x[3]))

# k의 위치, k의 금은동 개수 리스트 찾기
k_idx = 0
k_data = []

for j in range(len(data_list_sorted)):
    if data_list_sorted[j][0] == k:
        k_idx = j
        k_data = data_list_sorted[j][1:]
        break

# 등수 찾기
k_rank_count = 0

for d in data_list_sorted:
    if d[1:] != k_data:
        k_rank_count += 1
        continue
    else:
        k_rank_count += 1
        print(k_rank_count)
        break
