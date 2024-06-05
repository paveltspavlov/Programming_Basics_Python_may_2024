import array

text_to_convert = input().lower()

vowels = [
    array.array('u', ["a", "e", "i", "o", "u"]),
    array.array('i', [1, 2, 3, 4, 5])
]
index = 0
num = 0

for i in text_to_convert:
    if i in vowels:
        sum = i+vowels[index][num]
        i =+i
        index += 1
        num += 1
        num += 1
        print(sum)
    else:
        index += 1
        num += 1
        num += 1
        continue
