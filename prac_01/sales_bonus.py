LOW_BONUS = 0.1
HIGH_BONUS = 0.15
WELL_SALES = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < WELL_SALES:
        bonus = sales * LOW_BONUS
        print(f"Bonus is {bonus}")
    else:
        bonus = sales * HIGH_BONUS
        print(f"Bonus is {bonus}")
        sales = float(input("Enter sales: $"))
print("Quit")