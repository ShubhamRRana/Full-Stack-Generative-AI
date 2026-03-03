choice = input("Enter the snack you want to order: ").lower()
if choice == "samosa" or choice == "cookie":
    print("Order accepted and confirmed")
else:
    print(f"{choice} is out of stock.")
    