numbers_count = int(input())
i = 0
printable_num = 0

while i < numbers_count:
    number = int(input())
    printable_num += number
    i += 1

print(printable_num)
