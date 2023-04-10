# 10810
n, m = list(map(int, input().split()))

rule = [0 for _ in range(m)]
for j in range(m):
    rule[j] = list(map(int, input().split()))

basket = list(0 for i in range(n))

for j in rule:
    for j in range(j[0]-1, j[1]):
        basket[j] = j[2]
print(*basket)
