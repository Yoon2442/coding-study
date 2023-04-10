# 25206
score = []
for _ in range(20):
    score.append(input().split())

count = 0
sum = 0

for row in score:
    credit = row[1]
    grade = row[2]
    grade_score = 0

    if grade == "P":
        pass
    else:
        if grade == "A+":
            grade_score = 4.5
        elif grade == "A0":
            grade_score = 4.0
        elif grade == "B+":
            grade_score = 3.5
        elif grade == "B0":
            grade_score = 3.0
        elif grade == "C+":
            grade_score = 2.5
        elif grade == "C0":
            grade_score = 2.0
        elif grade == "D+":
            grade_score = 1.5
        elif grade == "D0":
            grade_score = 1.0
        elif grade == "F":
            grade_score = 0.0
        sum = sum+(float(credit)*float(grade_score))
        count = count+float(credit)
print(sum/count)
