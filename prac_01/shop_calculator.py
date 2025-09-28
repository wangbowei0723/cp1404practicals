total_price = 0
DISCOUNT = 0.9

items_number= int(input("Number of items:"))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items:"))
for i in range(items_number):
    items_price= float(input("Price of item:"))
    total_price += items_price
if total_price > 100:
    discount_price = total_price * DISCOUNT
    print(f"Total price for {items_number} items is ${discount_price:.2f}")
else :
    print(f"Total price for {items_number} items is ${total_price:.2f}")