# value = 13
# remainder = value % 5
# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# := -> This is walrus operator
# value = 13
# if remainder := value%5 :
#     print(f"Not divisible, remainder is {remainder}")
    
# avaiable_sizes = ["small","medium","large"]
# if (requeste_size := input("Enter you chai cup size:")) in avaiable_sizes:
#     print(f"Ordering {requeste_size} chai")
# else:
#     print(f"Chai not available for {requeste_size} size")

flavours = ["masala", "ginger", "lemon", "mint"]
print(f"Availabe flavours : {flavours}")

while (flavour := input("What tea flavour you want: ")) not in flavours:
    print(f"Sorry, {flavour} chai is not available")
print(f"You choose {flavour} chai")