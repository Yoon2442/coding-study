# 10812
n, m = list(map(int, input().split()))
rule = [0 for _ in range(m)]
for j in range(0, m):
    rule[j] = list(map(int, input().split()))
basket = [i for i in range(1, n+1)]
for row in rule:
    begin = row[0]-1
    end = row[1]
    mid = row[2]-1

    left = basket[begin:mid]
    right = basket[mid:end]

    del basket[begin:end]
    rotated_list = [*right, *left]
    basket[begin:begin] = rotated_list

print(*basket)
