# # function parameters
# def greet(name):
#     msg = "Hello, " + name
#     print(msg)


# greet("Abigail")


# # type hints
# def add(x: int, y: int) -> int:
#     return x + y

# result = add(6, 9)
# print(result)

# # default arguments
# def greet(greeting="Hello"):
#     print(greeting + " Gowah!")

# greet("Hi")
# greet()

# # if statements

# account_balance = int(input("Enter your Account Balance: "))

# if account_balance < 0:
#     print("Your Account is OVERDRAWN")
# elif account_balance > 1000000:
#     print("ALERT, ACCOUNT EXCEEDS $1MILLION")
# else:
#     print(f"Your Account balance is {account_balance:,}")

# # while loop
# i = 5
# while i < 10:
#     print("I love python")
#     i += 1

# x = 10
# while x < 90:
#     print(x)
#     x += 10

# # for loop
# for i in range(10, 21, 2):
#     print(i)

# #  reverse
# for i in range(20, 10, -1):
#     print(i)

# for i in reversed(range(10, 21)):
#     print(i)

# # nested loop
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# # string looping
# def print_string_char(my_string: str) -> None:
#     for i in range(len(my_string)):
#         print(my_string[i])

# print_string_char("Emma")

def print_string_char(my_string: str) -> None:
    for char in my_string:
        print(char)

print_string_char("Emma")