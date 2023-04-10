# 10988
s = input()
checker = 0
for j in range(0, len(s)//2):
    if s[j] == s[len(s)-1-j]:
        checker += 0
    else:
        checker += 1
if checker > 0:
    print(0)
else:
    print(1)
