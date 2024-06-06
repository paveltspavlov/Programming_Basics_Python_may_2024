numbers_count = int(input())

numbers_under_200 = 0
numbers_under_400 = 0
numbers_under_600 = 0
numbers_under_800 = 0
numbers_under_1000 = 0
number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
number_5 = 0
total = 0
i = 0

for i in range(numbers_count):
    number = int(input())
    if number < 200:
        numbers_under_200 += 1
    elif 200 <= number < 400:
        numbers_under_400 += 1
    elif 400 <= number < 600:
        numbers_under_600 += 1
    elif 600 <= number < 800:
        numbers_under_800 += 1
    else:
        numbers_under_1000 += 1

    total = numbers_under_200 + numbers_under_400 + numbers_under_600 + numbers_under_800 + numbers_under_1000


print(f"{((numbers_under_200 / total) * 100):.2f}%")
print(f"{((numbers_under_400 / total) * 100):.2f}%")
print(f"{((numbers_under_600 / total) * 100):.2f}%")
print(f"{((numbers_under_800 / total) * 100):.2f}%")
print(f"{((numbers_under_1000 / total) * 100):.2f}%")
