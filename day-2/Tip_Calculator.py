#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the Tip Calculator!")
initial_bill = float(input("What was the total bill?: "))

tip = int(input("What percentage tip ypu like to give? 10, 12 or 15: "))
split = int(input("How many people to split the bill?: "))
new_tip = tip / 100
amount_tip = initial_bill * new_tip

total_bill = amount_tip + initial_bill
each_person_bill = round(total_bill / split, 2)

print(f"Each person should pay ${each_person_bill}")

