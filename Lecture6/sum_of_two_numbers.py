lower_bound = int(input())
upper_bound = int(input())
magic_number = int(input())
combination_counter = 0
is_found = False

for i in range(lower_bound, upper_bound + 1):
    for j in range(lower_bound, upper_bound + 1):
        combination_counter += 1
        if i + j == magic_number:
            print(f"Combination N:{combination_counter} ({i} + {j} = {magic_number})")
            is_found = True
            break

    if is_found:
        break
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
