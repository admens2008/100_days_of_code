# A prg to calculate Life in days, weeks and months if the maximum age is 90
age = int(input("What is your current age? "))

years_remaining = (90 - age)
# print(rest)

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"Your {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left")