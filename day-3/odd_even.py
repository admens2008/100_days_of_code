# A prg that works out whether if a given number is an odd or even number

number = int(input("Provide your number: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")