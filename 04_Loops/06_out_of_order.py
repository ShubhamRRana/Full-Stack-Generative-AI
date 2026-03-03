flavour = ["Ginger","Out of stock","Lemon","Discontinued", "Tulsi"]

for flavour in flavour:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    
print("Outside the loop")