# A prg to calculate the sum of all the even numbers from 1 to 100

sum_even_numbers = 0
for number in range(0, 101, 2):
    sum_even_numbers += number
print(sum_even_numbers)
