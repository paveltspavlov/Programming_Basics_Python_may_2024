actor = input()
points = float(input())
number_of_judges = int(input())

i = 0
j = 0
judge_final = points
judge_name_len = 0

for i in range(1, number_of_judges):
    judge_name = input()
    for j in range(judge_name_len):

        judge_name_len = len(judge_name)
        judge_grade = float(input())
        judge_total_grade = float(judge_grade * len(judge_name))
        judge_final += judge_total_grade
        i += 1
        j +=1

        if judge_final >= 1250.5:
            print(f"Congratulations, {actor} got a nominee for leading role with {judge_final}")
            break
        elif judge_final < 1250.5:
            print(f"Sorry, {actor} you need {1250.5 - judge_final}")
            continue
