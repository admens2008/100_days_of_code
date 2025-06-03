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

# # chapter project
# # multiplication table

# is_valid = False
# while not is_valid:
#     num = int(input("Enter number between 1 and 19: "))

#     if num > 0 and num < 20:
#         is_valid = True

# for row in range(1, num + 1):
#     for product in range(row, row * (num + 1), row):
#         print(f"{product:4}", end="")
#     print()

# x = float(3490)
# y = 3.14159

# print(f"x is {x:4.2f}")
# print(f"y is {y:4.2f}")
# print(f"x + y = {(x + y):.2f}")

# s = "How many goats could a goat goat goat if a goat could goat"

# print(s.count("goat"))

# s = "The quick brown fox jumps over the lazy dogs"
# vowel = ['a', 'e', 'i', 'o', 'u']
# for c in s:
#     if c[0] in vowel:
#         c = c.upper()
#     else:
#         c = c.lower()
#     print(c, end="")
# print()

# string = input("Enter a word: ")
# is_valid = False
# while not is_valid:

    
#     num = int(input(f"Enter a number between 0 and {len(string) - 1}: "))

#     if num < len(string):
#         is_valid = True
#     else:
#         print("NUmber out of range")
# char = string[num]
# print(char)

# string = input("Enter a word: ")

# is_valid = False
# while not is_valid:

#     num_1 = int(input(f"Enter first number between 0 and {len(string)}: "))
#     num_2 = int(input(f"Enter second number between 0 and {len(string)}: "))

#     if num_1 <= len(string) and num_2 <= len(string):
#         is_valid = True
#     else:
#         print("Enter a number within range")
# result = string[num_1: num_2]
# print(result)

# s = "The quick brown fox jumps over the lazy dogs."

# s2 = ""

# for c in s.lower():
# 	if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
# 		c = c.upper()

	# A more concise way to write the above line is with "in", something
	# we haven't discussed yet:
	#if c in "aeiou":
	#	c = c.upper()

	# Build the new string a character at at time:
# 	s2 += c

# print(s2)

# s = input("Enter a string: ")

# valid_input = False

# while not valid_input:
# 	i = input(f"Enter a number (0 to {len(s)-1}): ")

# 	i = int(i)

# 	# Set valid_input directly with Boolean expression
# 	valid_input = i >= 0 and i <= len(s)-1

# print(f'Character at index {i} is "{s[i]}"')

# s = input("Enter a string: ")

# valid_input = False

# while not valid_input:
# 	i0 = input(f"Enter a number (0 to {len(s)}): ")

# 	i0 = int(i0)

# 	# Set valid_input directly with Boolean expression
# 	valid_input = i0 >= 0 and i0 <= len(s)

# valid_input = False

# while not valid_input:
# 	i1 = input(f"Enter a number ({i0} to {len(s)}): ")

# 	i1 = int(i1)

# 	# Set valid_input directly with Boolean expression
# 	valid_input = i1 >= 0 and i1 <= len(s)

# print(f'Slice from {i0} to {i1} is "{s[i0:i1]}"')