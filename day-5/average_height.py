# A prg that calculates the average student height from a list of heights

# student_heights = [180, 124, 165, 173, 189, 169, 146]
student_heights = input("provide ur numbers: ").split()

for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

# print(student_heights)

sum = 0
for height in student_heights:
    
    sum += height
   
  
# print(sum)

number = 0
for n in student_heights:
    number += 1
# print(number)

average_height = sum / number
print(f"Average height is {round(average_height, 2)}")