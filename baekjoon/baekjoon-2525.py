# 2525
time = list(map(int, input().split()))
cooking_time = int(input())
minute = time[1]+cooking_time
hour = time[0]

if minute > 59:
    hour = time[0]+minute//60
    minute = minute % 60

if hour > 23:
    hour = hour-24

print(hour, minute)
