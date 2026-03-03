users = [
    {"name":"Shubham", "total":426, "coupon":"QWE"},
    {"name":"Ajay", "total":356, "coupon":"ASD"},
    {"name":"Dinesh", "total":138, "coupon":"ZXC"}
]

discounts = {
    "QWE":(0.2,0),
    "ASD":(0.1,0),
    "ZXC":(0,10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    finalAmount = user["total"] - discount
    print(f"{user["name"]} paid {user["total"]} got discount of {discount} and paid final amount as {finalAmount}")