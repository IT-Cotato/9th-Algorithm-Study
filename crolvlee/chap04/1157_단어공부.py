word = str(input())
word = word.upper()

my_dict = {}

for i in word:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1


max_value = max(my_dict.values())
max_keys = [key for key, value in my_dict.items() if max_value == value]

if len(max_keys) > 1:
    print("?")
else:
    print(max_keys[0])