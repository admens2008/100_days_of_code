# x = int(input("Enter a number between 50 and 59: "))

# if x >= 50 and x <= 59:
#     print(f"{x} is between 50 and 59") 
# else:
#     print(f"{x} is outside 50 and 59")

# # while loop

# x = 1200

# while x < 1211:
#     print(x)
#     x += 1
# print("All done")

# x = int(input("Enter a number between 5 and 50: "))

# while x < 5 or x > 50:
#     x = int(input("Enter a number between 5 and 50: "))

# print(f"WELL DONE! {x} is between 5 and 50")

# # for loop
# for i in range(10):
#     print(i)

# for i in range(5, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# Chapter Project

input_valid = False

while not input_valid:
    x = int(input("Enter a number between 5 and 50: "))

    if x >= 5 and x <= 50:
        input_valid = True
    else:
        print("Number must be between 5 and 50")

for i in range(x):
    if i < 30:
        print("#", end="")
    else:
        print("*", end="")
print()