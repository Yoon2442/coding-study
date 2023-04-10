# 10813
n, m = list(map(int, input().split()))
basket = list(i+1 for i in range(n))

rule = [0 for _ in range(m)]
for j in range(m):
    rule[j] = list(map(int, input().split()))

for j in rule:
    temp = basket[j[0]-1]
    basket[j[0]-1] = basket[j[1]-1]
    basket[j[1]-1] = temp

print(*basket)
