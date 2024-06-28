bad_grades = int(input())
bad_grades_count = 0
avg_score = 0
total_score = 0
total_grades = 0
exam_name = ""
last_problem = ""

while exam_name != "Enough":
    exam_name = input()

    if exam_name == "Enough":
        break
    grade = int(input())

    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades:
            break

    total_score += grade
    last_problem = exam_name
    total_grades += 1

average = total_score / total_grades

if bad_grades_count < bad_grades:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {total_grades}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades} poor grades.")
