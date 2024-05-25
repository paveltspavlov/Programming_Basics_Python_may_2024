from math import pi
shape = input()

if shape == "square":
    side = float(input())
    area = float(side * side)
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = float(side_a * side_b)
elif shape == "circle":
    radius = float(input())
    area = float(pi * (radius * radius))
elif shape == "triangle":
    side = float(input())
    height = float(input())
    area = float(side * height / 2)


print(f"{area:.3f}")