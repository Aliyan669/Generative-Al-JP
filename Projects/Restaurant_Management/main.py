menu={
    "Zinger":200,
    "Roll": 150,
    "Fries": 500,
    "Coffee":100
}

print("Welcome to Our Restaurant")
for key,val in menu.items():
    print(key,' Rs',val)
    
total_amount = 0 

order_1 = input("Enter the name of item you want to order=")

if order_1 in menu:
    total_amount += menu[order_1]
    # print(total_amount)
    print("Your item", order_1, "has been added to your order")
else:
   print("Order item", order_1, "is not available")


more_order = input("Do You want to add another item? (Yes/No) ")

if more_order == "Yes" or more_order == "yes":
    order_2 = input("Enter the name of second item you want to order=")
    if order_2 in menu:
        total_amount += menu[order_2]
        print("Your item", order_2, "has been added to your order")
    else:
        print("Orderitem", order_2, "is not available")
    
    
print(total_amount)