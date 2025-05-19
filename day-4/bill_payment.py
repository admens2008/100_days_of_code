import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
# print(length)
choice = random.randint(0, length - 1)
# print(choice)
print(f"{names[choice]} is going to buy the meal today")