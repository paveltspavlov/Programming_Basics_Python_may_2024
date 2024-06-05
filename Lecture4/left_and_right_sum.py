num_inputs = int(input())
i = 0

left_input = 0
right_input = 0

while i < num_inputs:
    left_input += int(input())
    i += 1

i = 0

while i < num_inputs:
    right_input += int(input())
    i += 1

if left_input == right_input:

    print(f"Yes, sum = {left_input}")

elif left_input > right_input:
    diff1 = left_input - right_input
    print(f"No, diff = {diff1}")
elif left_input < right_input:
    diff2 = right_input - left_input
    print(f"No, diff = {diff2}")
