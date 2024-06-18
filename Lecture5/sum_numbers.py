number = int(input())
num = 0
buff = 0

while number != buff:
    num = int(input())
    buff += num
    if number <= buff:
        break

print(buff)
