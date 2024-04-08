n=int(input())

one_time=0 # 팀1이 이기는 시간
two_time=0 # 팀2가 이기는 시간
flag=0

# 팀1이 이기고 있다가 비기게 되면 (total - 팀1이 이기기 시작한 시간) - (total - 팀2가 골 넣어서 비기기 시작한 시간)

for i in range(n):
    team, time=input().split()
    m,s=map(int, time.split(':'))
    s = 60 * m + s
    total = 48 * 60
    if team == '1':
        if flag==0: # 처음 이기려고 함
            one_time += total - s # 이기기 시작한 시간
        flag += 1 # 팀1이 이김
        if flag==0: 
            if two_time>0: # 팀2가 이기고 있다가 팀1이 골 넣어서 동점되기 시작 -> 팀2 이기는 시간 멈춰주기
                two_time=two_time-(total - s) 
    else: # 팀2
        if flag==0: # 처음 이기려고 함
            two_time += total - s # 이기기 시작한 시간
        flag -= 1 # 팀2가 이김
        if flag==0:
            if one_time>0: # 팀1이 이기고 있다가 팀2가 골 넣어서 동점되기 시작 -> 팀1 이기는 시간 멈춰주기
                one_time=one_time-(total - s)


print('{:0>2}:{:0>2}'.format(one_time//60,one_time%60))
print('{:0>2}:{:0>2}'.format(two_time//60,two_time%60))