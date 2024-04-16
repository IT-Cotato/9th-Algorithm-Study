N = int(input())

score = {1: 0, 2: 0} # 득점 현황
scoreTime = {1: 0, 2: 0} # 득점 시간
leadTime = {1: 0, 2: 0} # 이기고 있던 시간
lead = 0 # 리드중인 팀 / 0: 동점 상황

for i in range(N):
    # team, time 모두 int 형식으로 변환
    team, time = input().split()
    team = int(team)
    minute, second = map(int, time.split(':'))
    time = minute*60 + second
    score[team] += 1

    # 동점 상황에서 특정 팀이 득점한 경우
    if lead == 0: 
        scoreTime[team] = time
        lead = team
    # 입력받은 득점으로 동점이 된 경우
    elif lead != 0 and score[1] == score[2]:
        leadTime[lead] = time - scoreTime[lead] # 이기고 있던 시간 = 입력받은 득점 시간 - 이기고 있던 팀의 득점 시간
        lead = 0

# 입력 종료 후 이긴 팀이 있는 경우
if lead != 0:
    leadTime[lead] += 60*48 - scoreTime[lead] # (경기 종료 시간 - 이긴 팀의 득점 시간) 추가

print("%02d:%02d" %(leadTime[1]//60, leadTime[1]%60))
print("%02d:%02d" %(leadTime[2]//60, leadTime[2]%60))