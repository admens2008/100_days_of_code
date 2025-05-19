print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

full_name = name1 + name2
# print(full_name)
t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')
first_digit = t + r + u + e
# fist_digit = str(first_digit)
# print(first_digit)
# print(type(first_digit))
l = full_name.count('l')
o = full_name.count('o')
v = full_name.count('v')
e = full_name.count('e')
second_digit = l + o + v + e
# second_digit = str(second_digit)
# print(second_digit)
# print(type(second_digit))
score = str(first_digit) + str(second_digit)
score = int(score)
if score < 10 or score > 90:
    print(f"Your love score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your love score is {score}, you are alright together")
else:
    print(f"Your love score is {score}")
# score = first_digit + second_digit
# print(first_digit + second_digit)