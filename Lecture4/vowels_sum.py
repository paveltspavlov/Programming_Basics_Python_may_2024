import array

text_to_convert = array.array(input())

a= 1
e = 2
i = 3
o = 4
u = 5

result = 0
i = 0
if i < text_to_convert.len():
    if a == text_to_convert(i):
        result += a
        i += 1
    elif e in text_to_convert:
        result += e
        i += 1
    elif i in text_to_convert:
        result += i
        i += 1
    elif o in text_to_convert:
        result += o
        i += 1
    elif u in text_to_convert:
        result += u
        i += 1

print(result)
