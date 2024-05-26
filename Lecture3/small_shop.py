item = input()
town = input()
quantity = float(input())

if town == "Sofia":
    if item == "coffee":
        print(quantity * 0.50)
    elif item == "water":
        print(quantity * 0.80)
    elif item == "beer":
        print(quantity * 1.20)
    elif item == "sweets":
        print(quantity * 1.45)
    elif item == "peanuts":
        print(quantity * 1.60)
elif town == "Plovdiv":
    if item == "coffee":
        print(quantity * 0.40)
    elif item == "water":
        print(quantity * 0.70)
    elif item == "beer":
        print(quantity * 1.15)
    elif item == "sweets":
        print(quantity * 1.30)
    elif item == "peanuts":
        print(quantity * 1.50)
elif town == "Varna":
    if item == "coffee":
        print(quantity * 0.45)
    elif item == "water":
        print(quantity * 0.70)
    elif item == "beer":
        print(quantity * 1.10)
    elif item == "sweets":
        print(quantity * 1.35)
    elif item == "peanuts":
        print(quantity * 1.55)
