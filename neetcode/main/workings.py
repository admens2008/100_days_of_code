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

# def print_string_char(my_string: str) -> None:
#     for char in my_string:
#         print(char)

# print_string_char("Emma")

# # string concatenation
# def concatenate(s1: str, s2: str) -> str:
#     s3 = s1 + s2
#     if len(s3) > 10:
#         return "Too long"
#     return s3

# print(concatenate("Hello", " world"))

# # string slicing
# my_string = "international"
# print(my_string[0:5])
# print(my_string[::-1])

# # strings are immutable
# # if we want to delete index 1, we'll need to build another string
# message = "I will never change"
# before_second = message[:1]
# after_second = message[2:]
# third_message = before_second + after_second
# print(third_message)

# def remove_fourth_char(word: str) -> str:
#     before_fourth = word[:3]
#     after_fourth = word[4:]
#     return before_fourth + after_fourth

# print(remove_fourth_char("Neetcode"))

# # string formatting

# def say_goodbye(name: str, hour: int) -> str:
#     return (f"Goodbye, {name}. See you again at {hour} o'clock.")

# print(say_goodbye("Bob", 12))

# # Lists
# # a collection of items stored in a specific order
# # Lists are immutable unlike strings

# my_list = [1, 7, 5, 4, 3, 2]
# print(my_list[1]) ## print second element
# print(len(my_list))

# if 2 not in my_list:
#     print("2 is NOT in the list")
# print("2 is PRESENT")

# def check_list_empty(my_list) -> bool:
#     if len(my_list) < 1:
#         return True
#     return False

# my_list = [3, 2, 8, 6, 4, 3]

# print(check_list_empty(my_list))

# def check_element_in_list(my_list, element) -> bool:
#     if element not in my_list:
#         return False
#     return True

# print(check_element_in_list(my_list, 4))

# for i in range(len(my_list)):
#     print(my_list[i])

# def count_x(list, x) -> int:
#     result = 0
#     for n in list:
#         if n == x:
#             result += 1
#     return result

# print(count_x(my_list, 3))

# List functions

# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))

# def get_sum(list) -> int:
#     total = 0
#     for num in list:
#         total += num
#     return total

# def get_max(list) -> int:
#     max_num = 0
#     for num in list:
#         if num > max_num:
#             max_num = num
#     return max_num



# def get_min(list) -> int:
#     min_num = list[0]
#     for num in list:
#         if num < min_num:
#             min_num = num
#     return min_num

# print(get_sum(my_list))
# print(get_max(my_list))
# print(get_min(my_list))