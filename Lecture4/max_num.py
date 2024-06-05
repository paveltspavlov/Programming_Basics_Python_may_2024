import math

numbers_count = int(input())

i = 0
numbers = []
while i in range(numbers_count):
    number = int(input())
    numbers.append(number)
    i += 1
smallest_num = min(numbers)
highest_num = max(numbers)

print(f"Max number: {highest_num}")
print(f"Min number: {smallest_num}")
