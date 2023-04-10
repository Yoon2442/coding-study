# 25304
total = int(input())
category = int(input())
arr = list(0 for i in range(0, category))
for row in range(0, category):
    arr[row] = list(map(int, input().split()))

result = 0
for row in range(0, category):
    result = result+arr[row][0]*arr[row][1]

if total == result:
    print("Yes")
else:
    print("No")
