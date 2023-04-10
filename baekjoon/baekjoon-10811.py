# 10811
n, m = list(map(int, input().split()))

basket = [i+1 for i in range(0, n)]
rule = [0 for _ in range(m)]
for j in range(m):
    rule[j] = list(map(int, input().split()))

for j in rule:
    first = j[0]-1
    last = j[1]-1
    temp = [basket[k] for k in range(first, last+1)]
    temp.reverse()
    for j in range(first, last+1):
        basket[j] = temp[j-first]
print(*basket)
