# 10807
n = int(input())
arr = list(map(int, input().split()))
v = int(input())
count = 0

for j in arr:
    if j == v:
        count += 1

print(count)
