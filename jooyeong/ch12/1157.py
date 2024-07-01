word = input().lower() # 대소문자 구분하지 않으므로 소문자로 저장
word_list = list(set(word))
cnt = []

for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())