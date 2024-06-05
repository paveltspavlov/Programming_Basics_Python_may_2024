text_to_convert = input()
a = 1
e = 2
i = 3
o = 4
u = 5

result = 0
for char in text_to_convert:
    if char == 'a':
        result += a
    elif char == 'e':
        result += e
    elif char == 'i':
        result += i
    elif char == 'o':
        result += o
    elif char == 'u':
        result += u

print(result)