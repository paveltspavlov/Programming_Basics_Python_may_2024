num_inputs = int(input())
input_list = []

for i in range(num_inputs):
    input_list.append(int(input()))

even = 0
odd = 0

for i, num in enumerate(input_list):
    if i % 2 == 0:
        even += num
    else:
        odd += num
    i += 1

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
elif even > odd:
    diff = even - odd
    print("No")
    print(f"Diff = {diff}")
else:
    diff = odd - even
    print("No")
    print(f"Diff = {diff}")