'''
Expand on the previous NTUC Cashier program

This time, the customer can choose up to 3 items to buy
e.g. apples, oranges, and eggs

You can set a price for each item.
1. Ask the customer what they are buying
2. Ask the customer how many units of the item are they buying
3. Keep asking the customer until the customer says "enough"
4. Calculate the total purchase of the customer
'''
apple = 1
feastable = 3.5
milk = 1.3
total = 0     # for total amount to pay
answer = input("do you have any item in your basket?")
while answer == "yes":
    item = input("what is the item?")
    quantity = input("how many of that?")
    quantity = int(quantity)
    if item == "apple":
        price = apple * quantity
        total = total + price
    if item == "milk":
        price = milk * quantity
        total = total + price
    
    answer = input("do you have any item in your basket?")
print("thank you for visiting NTUC")
print("you have to pay me $", total)