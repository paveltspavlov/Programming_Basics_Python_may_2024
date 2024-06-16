group_count = int(input())
total_people = 0
musala_group = 0
montblanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0

for i in range(group_count):
    group = int(input())
    if group <= 5:
        musala_group += group
        total_people += group
    elif group >= 6 and group <= 12:
        montblanc_group += group
        total_people += group
    elif group >= 13 and group <= 25:
        kilimanjaro_group += group
        total_people += group
    elif group >= 26 and group <= 40:
        k2_group += group
        total_people += group
    elif group >= 41:
        everest_group += group
        total_people += group

    i += i
print(f"{musala_group / total_people * 100:.2f}%")
print(f"{montblanc_group / total_people * 100:.2f}%")
print(f"{kilimanjaro_group / total_people * 100:.2f}%")
print(f"{k2_group / total_people * 100:.2f}%")
print(f"{everest_group / total_people * 100:.2f}%")
