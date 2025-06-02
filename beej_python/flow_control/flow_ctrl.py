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

# input_valid = False

# while not input_valid:
#     x = int(input("Enter a number between 5 and 50: "))

#     if x >= 5 and x <= 50:
#         input_valid = True
#     else:
#         print("Number must be between 5 and 50")

# for i in range(x):
#     if i < 30:
#         print("#", end="")
#     else:
#         print("*", end="")
# print()

# is_even = False

# while not is_even:
#     num = int(input("Enter an even number: "))

#     if num % 2 == 0:
#         is_even = True
#     else:
#         print(f"{num} ISN'T an even number")

# print(f"Congrats {num} is an EVEN number")

# sum of numbers from to (and including) 1000

# sum = 0
# for num in range(1, 1001):
#     sum += num
# print(sum)


# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# for i in range(x, y + 1):
#     if not i % 2 == 0:
#         print(i, end=" ")
# print()

# done = False
# while not done:
#     x = input("Enter a number or type 'quit': ")
#     if x == "quit":
#         done = True
#     else:
#         x = int(x)
#         print(x, "times 10 is", x * 10)

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# if x % 2 == 0:
#     x+= 1

# for i in range(x, y + 1, 2):
#     print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)