bad_grades = int(input())
bad_grades_count = 0
avg_score = 0
total_score = 0
exam_name = ""

while exam_name != "Enough":
    exam_name = input()
    grade = int(input())
    if exam_name == "Enough":
        break
    elif grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades:
            print(f"You need a break, {bad_grades} poor grades.")
            break
        continue
    else:
        avg_score += grade

print(f"Average score: {avg_score / grade}")
print(f"Last problem: {exam_name}")
