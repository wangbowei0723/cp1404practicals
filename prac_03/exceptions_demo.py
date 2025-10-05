"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
ANSWER:when you enter letters or symbols(such as "K" or ">").

2. When will a ZeroDivisionError occur?
ANSWER:The denominator that you entered is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
ANSWER:Could, as python code below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("denominator cannot be 0, please enter again:")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
