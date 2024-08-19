s = input()
a = 0
for i in range(len(s)-1):
    if s[i+1] != s[i] :
        a += 1
if a%2 == 0:
    print(a//2)
else :
    print(a//2+1)