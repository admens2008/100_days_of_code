is_valid = False
while not is_valid:

    string = input("Enter a word: ")
    num = int(input("Enter a number: "))

    if num < len(string):
        is_valid = True
    else:
        print("NUmber out of range")
char = string[num]
print(char)
