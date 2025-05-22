# A prg that print each item from 1 to 100 in turn. when the num is divisible by 3, print Fizz rather, print Buzz if divisible by 5. print FizzBuzz if divisible by both 3 and 5

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)