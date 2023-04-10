# 9086
T = int(input())
test_case = []
for j in range(0, T):
    test_case.append(input())

for j in test_case:
    print(j[0]+j[len(j)-1])
