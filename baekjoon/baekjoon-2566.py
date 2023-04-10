# 2566
matrix = []
for row in range(0, 9):
    row = list(map(int, input().split()))
    matrix.append(row)

row_num = 0
col_num = 0
value = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if (value <= matrix[row][col]):
            row_num = row
            col_num = col
            value = matrix[row][col]

print(value)
print(row_num+1, col_num+1)
