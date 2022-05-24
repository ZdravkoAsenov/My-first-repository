temperature = float(input())
if temperature > 26.00 and temperature < 35.00:
    print("Hot")

if temperature > 20.1 and temperature < 25.9:
    print("Warm")

if temperature > 15.00 and temperature < 20.00:
    print("Mild")

if temperature > 12.00 and temperature < 14.9:
    print("Cold")

if temperature > 5.00 and temperature < 11.9:
    print("Cold")
else:
    print("unknown")