name = input()
grade = 0
sum_score = 0
average_score = 0
score = 0

while grade < 12:
    score = float(input())
    if 4 <= score <= 6:
        sum_score += score
        grade += 1
    elif 2 <= score < 4:
        grade += 1
        print(f"{name} has been excluded at {grade} grade")
        sum_score += score
        break
    average_score = sum_score / 12

if grade >= 12:
    print(f"{name} graduated. Average grade: {average_score:.2f}")
