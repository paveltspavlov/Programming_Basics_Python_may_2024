width = int(input())
length = int(input())
pieces = width * length
total_pieces_taken = 0
diff = 0

while True:
    command = input()
    if command == "STOP":
        break

    total_pieces_taken += int(command)
    pieces -= int(command)

    if total_pieces_taken > width * length:
        diff = total_pieces_taken - (width * length)
        break

if pieces >= 0:
    print(f"{pieces} pieces are left.")
elif pieces < 0:
    print(f"No more cake left! You need {pieces * (-1)} pieces more.")
