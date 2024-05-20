n = int(input())

schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

profit = [0 for _ in range(n+1)] # i번째 날짜까지의 최대 이익

for i in range(n):
    # 상담 가능한 모든 날짜:
    # (i일 + i번째 상담 시간)부터 마지막 날까지 
    for j in range(i + schedule[i][0], n + 1): 
        if profit[j] < profit[i] + schedule[i][1]: # i번째 상담을 진행했을 때 이익이 더 크다면 상담 진행   
            profit[j] = profit[i] + schedule[i][1]

print(profit[-1]) # 마지막 날짜