# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height * height))
# print(bmi)bmi > 30 and bmi 

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
if bmi < 18.5:
    print("You're underweight")

# Over 18.5 but below 25 they have a normal weight
elif bmi < 25:
    print("You have a normal weight")

# Over 25 but below 30 they are slightly overweight
elif bmi < 30:
    print("You're slightly overweight")

# Over 30 but below 35 they are obese
elif bmi < 35:
    print("You're obese")

# Above 35 they are clinically obese.
else:
    print("You're clinically obese")