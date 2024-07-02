coins = int(float(input()) * 100)

counter = 0

while coins > 0:

    counter += 1
    if coins >= 200:
        coins -= 200
    elif 100 <= coins < 200:
        coins -= 100
    elif 50 <= coins < 100:
        coins -= 50
    elif 20 <= coins < 50:
        coins -= 20
    elif 10 <= coins < 20:
        coins -= 10
    elif 5 <= coins < 10:
        coins -= 5
    elif 2 <= coins < 5:
        coins -= 2
    elif coins >= 1:
        coins -= 1

print(counter)
