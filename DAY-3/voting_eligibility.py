# Program   : Voting Eligibility Checker
# Topic     : Conditional Statements
# Approach  : Check age using if-elif-else conditions

age = int(input("Enter Age : "))

if age < 0:
    print("Invalid Input")
elif age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
