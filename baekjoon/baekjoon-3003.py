# 3003
chess = list(map(int, input().split()))
compare = [1, 1, 2, 2, 2, 8]
result = [0 for i in range(0, 6)]
for j in range(0, 6):
    result[j] = compare[j]-chess[j]
print(*result)
