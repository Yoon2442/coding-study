# 2480
numbers = list(map(int, input().split()))
one = numbers[0]
two = numbers[1]
three = numbers[2]
result = 0
if one == two and two == three:
    result = 10000+one*1000
elif one == two and two != three:
    result = 1000+one*100
elif two == three and three != one:
    result = 1000+two*100
elif three == one and one != two:
    result = 1000+three*100
else:
    max_value = max(numbers)
    result = max_value*100
print(result)
