#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
rand_password = ""

for _ in range(nr_letters):
    password += random.choice(letters)
# print(password)

for s in range(nr_symbols):
    password+= random.choice(symbols)
# print(password)

for n in range(nr_numbers):
    password+= random.choice(numbers)
# print(password)

# shuffle the password. first convert to list first
password_list = list(password)
random.shuffle(password_list)
# print(password_list)

char = ""
for _ in password_list:
    char += _
print(f"Your password is {char}")