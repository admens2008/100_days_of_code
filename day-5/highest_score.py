students_scores = input("Enter scores: ").split()

for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
               

# scores = [90, 4, 67, 12]

highest = 0
for i in students_scores:
    if i > highest:
        highest = i

print(f"The highest score in the class is: {highest}")
