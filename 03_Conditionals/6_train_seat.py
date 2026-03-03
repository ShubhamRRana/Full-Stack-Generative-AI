seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()
match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - AC and beds available")
    case "general":
        print("General - Cheapest option")
    case "luxury":
        print("Expensive option - Premium seats and meals")
    case _:
        print("Invalid seat type")
        
        