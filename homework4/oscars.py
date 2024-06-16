actor = input()
points = float(input())
number_of_judges = int(input())

i = 0
j = 0
judge_final = points
judge_name_len = 0


for i in range(number_of_judges):
    if judge_final < 1250.5:
        judge_name = input()
        judge_name_len = len(judge_name)
        judge_grade = float(input())
        judge_total_grade = float(judge_grade * judge_name_len)/2
        judge_final += judge_total_grade
        i += 1
        j += 1
    else:
        break

if judge_final >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {judge_final:.1f}!")
elif judge_final < 1250.5:
    losing_result = 1250.5 - judge_final
    print(f"Sorry, {actor} you need {losing_result:.1f} more!")
