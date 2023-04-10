# 5597
numbers = []
for j in range(0, 28):
    numbers.append(int(input()))
compare_list = [i+1 for i in range(0, 30)]
set1 = set(numbers)
set2 = set(compare_list)
print(min(set2-set1))
print(max(set2-set1))
