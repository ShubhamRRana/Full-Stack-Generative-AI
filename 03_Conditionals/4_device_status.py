isDevice = True
temperature = int(input("Entere a temperature : "))
if isDevice:
    if temperature > 35:
        print("High temperture alert")
    else:
        print("Temperature is normal")
else: 
    print("Device is offline")
    