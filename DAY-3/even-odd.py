# Program   : Check Even or Odd
# Topic     : Conditional Statements
# Approach  : Use modulus operator to check divisibility by 2

num = int(input("Enter a Number : "))

if num < 0:
    print("Invalid Input")
elif num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
