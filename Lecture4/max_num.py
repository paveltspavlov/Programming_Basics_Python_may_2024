numbers_count = int(input())

i = 0
numbers = []
while i < numbers_count:
    number = int(input())
    numbers[i] = [number]
    i += 1

print(numbers.max())
print(numbers.min())
