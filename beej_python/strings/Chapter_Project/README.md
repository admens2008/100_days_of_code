# 🧮 Python Multiplication Table Generator

A beginner-friendly Python program that prints a neatly formatted multiplication table based on user input (between 1 and 19). It uses basic control structures like loops and conditionals, making it a great practice project for Python beginners.

---

## 🚀 Getting Started

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository.
3. Open a terminal or command prompt.
4. Run the script using:


python multiplication_table.py

📌 Features
Prompts the user to enter a number between 1 and 19.

Validates input to ensure it's within the correct range.

Prints a neatly formatted multiplication table.

Uses nested loops and f-strings for clean output alignment.

🧠 How It Works (Algorithm)
1. Input Validation
The program uses a while loop to repeatedly ask the user to enter a number until they provide a valid one (1–19).

2. Generating the Table
The outer for loop controls the current row (1 through the input number).

The inner for loop calculates and prints the products for that row.

It uses a clever use of range():

python

range(row, row * (num + 1), row)

🔸 This gives all multiples of row like:
→ row × 1, row × 2, ..., row × num

String formatting (f"{product:4}") ensures the numbers align nicely in columns.

📋 Example Output
If the user enters 5, the output will be:
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25

🛠️ Concepts Used
while loop

for loop

range()

input() and int()

String formatting with f-strings

Nested loops

Conditional statements (if)

👤 Author
Emmanuel Adjei-Mensah
GitHub: @admens2008
📧 Email: adjeimensah@gmail.com

📄 License
This project is open-source and available under the MIT License.

📚 Learning Tip
Try modifying the range or format to display only even numbers, or experiment with different layouts to practice string formatting!

