num_one = int(input())
num_two = int(input())
operation = input()

result = 0

if operation == "+":
    if (num_one + num_two) % 2 == 0:
        print(f"{num_one} {operation} {num_two} = {num_one + num_two} - even")
    else:
        print(f"{num_one} {operation} {num_two} = {num_one + num_two} - odd")
elif operation == "-":
#    if num_one >= num_two:
        if (num_one - num_two) % 2 == 0:
            print(f"{num_one} {operation} {num_two} = {num_one - num_two} - even")
        else:
            print(f"{num_one} {operation} {num_two} = {num_one - num_two} - odd")

# In the task rescription the case where num_two is bigger than num_two is not specified
# and the Judge system returns an error for test 5
#    else:
#        if (num_one - num_two) % 2 == 0:
#            print(f"{num_two} {operation} {num_one} = {num_two - num_one} - even")
#        else:
#            print(f"{num_two} {operation} {num_one} = {num_two - num_one} - odd")
elif operation == "*":
    if (num_one * num_two) % 2 == 0:
        print(f"{num_one} {operation} {num_two} = {num_one * num_two} - even")
    else:
        print(f"{num_one} {operation} {num_two} = {num_one * num_two} - odd")
elif operation == "/":
    if num_two == 0:
        print(f"Cannot divide {num_one} by zero")
    else:
        result = float(num_one / num_two)
        print(f"{num_one} / {num_two} = {result:.2f}")
elif operation == "%":
    if num_two == 0:
        print(f"Cannot divide {num_one} by zero")
    else:
        result = num_one % num_two
        print(f"{num_one} % {num_two} = {result}")
