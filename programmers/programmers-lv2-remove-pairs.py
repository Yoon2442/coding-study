# Programmers - 짝지어 제거하기
s = "baabaa"
answer = 0
L = []
for j in s:
    if len(L) == 0:
        L.append(j)
        print("L append", j)
    else:
        if L[-1] == j:
            print("pop", L[-1])
            L.pop()
        else:
            L.append(j)
            print("L append", j)
    print(L)
if len(L) == 0:
    answer = 1
