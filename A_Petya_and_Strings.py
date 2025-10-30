str1 = input().lower()
str2 = input().lower()

flag = 0

for i in range(len(str1)):
    if ord(str1[i]) > ord(str2[i]):
        flag = 1
        break
    elif ord(str1[i]) < ord(str2[i]):
        flag = -1
        break

print(flag)
