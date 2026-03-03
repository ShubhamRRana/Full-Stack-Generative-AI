staff = [("Amit",16),("Zara",17),("Raj",15)]

for name, age in staff:
    if age<18:
        print(f"{name} is eligible for hiring")
        break
else: #else block is executed only if the for block does not break
    print("No one is eligible for hiring")