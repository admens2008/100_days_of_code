# A prg that calculates the Body Mass Index (BMI) from a user's weight and height
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#BMI = weight(kg)/ height * height(m)
# result rounded to 2 decimal places
print(round(weight / (height * height), 2)) 