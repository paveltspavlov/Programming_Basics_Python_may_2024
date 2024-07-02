free_width = int(input())
free_length = int(input())
free_height = int(input())
total_boxes = 0
total_free_space = 0
total_space = free_width * free_length * free_height
boxes = ''

while boxes != "Done":
    boxes = input()
    if boxes == "Done" or total_boxes > total_space:
        break

    total_boxes += int(boxes)

total_free_space = total_space - total_boxes

if total_space <= total_boxes:
    print(f"No more free space! You need {total_boxes - total_space} Cubic meters more.")
else:
    print(f"{total_free_space} Cubic meters left.")
