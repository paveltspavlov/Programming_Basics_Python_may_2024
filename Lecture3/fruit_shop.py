fruit = input()
day_of_week = input()
quantity = float(input())

if (day_of_week not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        or fruit not in ("banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes")):
    print("error")

elif day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
  if fruit == "banana":
      price = float(quantity * 2.50)
      print(f"{price:.2f}")
  elif fruit == "apple":
      price = float(quantity * 1.20)
      print(f"{price:.2f}")
  elif fruit == "orange":
      price = float(quantity * 0.85)
      print(f"{price:.2f}")
  elif fruit == "grapefruit":
      price = float(quantity * 1.45)
      print(f"{price:.2f}")
  elif fruit == "kiwi":
      price = float(quantity * 2.70)
      print(f"{price:.2f}")
  elif fruit == "pineapple":
      price = float(quantity * 5.50)
      print(f"{price:.2f}")
  elif fruit == "grapes":
      price = float(quantity * 3.85)
      print(f"{price:.2f}")

elif day_of_week in ("Saturday", "Sunday"):
  if fruit == "banana":
      price = float(quantity * 2.70)
      print(f"{price:.2f}")
  elif fruit == "apple":
      price = float(quantity * 1.25)
      print(f"{price:.2f}")
  elif fruit == "orange":
      price = float(quantity * 0.90)
      print(f"{price:.2f}")
  elif fruit == "grapefruit":
      price = float(quantity * 1.60)
      print(f"{price:.2f}")
  elif fruit == "kiwi":
      price = float(quantity * 3.00)
      print(f"{price:.2f}")
  elif fruit == "pineapple":
      price = float(quantity * 5.60)
      print(f"{price:.2f}")
  elif fruit == "grapes":
      price = float(quantity * 4.20)
      print(f"{price:.2f}")
