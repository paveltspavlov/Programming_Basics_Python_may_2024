fav_book = input()
counter = 0

while True:
    current_book = input()

    if current_book == fav_book:
        print(f"You checked {counter} books and found it.")
        break
    elif current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    counter += 1
