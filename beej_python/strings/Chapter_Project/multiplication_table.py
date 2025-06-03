# multiplication table
input_valid = False

while not input_valid:
    num = int(input("Enter a number between 1 and 19: "))

    if num > 0 and num < 20:
        input_valid = True
    print("Number out of range")

for row in range(1, num + 1):
    for product in range(row, row * (num + 1), row):
        print(f"{product:4}", end="")
    print()

    
