# # concatenate a string twith a number

# x = "Hello"
# y = str(3490)

# print(x + y)

# i = "3490"
# j = 1000
# print(int(i) + j)

# # slicing
# # a prg that prints out the first and last character of an input
# string = input("Enter a word: ")
# print(string[1: -1])

# # for loops with strings
# s = "Hello"

# for c in s:
#     print("character:", c)

# # enumerate
# s = "hello"

# for i, c in enumerate(s):
#     print("Character at index", i, "is:", c)

# chapter project
# multiplication table

is_valid = False
while not is_valid:
    num = int(input("Enter number between 1 and 19: "))

    if num > 0 and num < 20:
        is_valid = True