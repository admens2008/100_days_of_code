height = int(input("height: "))


if height >= 120:
    age = int(input("age: "))
    if age >= 18:
        print("You are free to enter")
    else:
        print("Too young to enter")
else:
    print("Grow taller and return")