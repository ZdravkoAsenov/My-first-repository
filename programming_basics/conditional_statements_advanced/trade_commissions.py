town = input()
seils = float(input())
comisiona = 0
if town == "Sofia":
    if 0 <= seils <= 500:
        comisiona = seils * 0.05
    elif 500 < seils <= 1000:
        comisiona = seils * 0.07
    elif 1000 < seils <= 10000:
        comisiona = seils * 0.08
    elif seils > 10000:
        comisiona = seils * 0.12
    else:
        print("error")

elif town == "Varna":
    if 0 <= seils <= 500:
        comisiona = seils * 0.045
    elif 500 < seils <= 1000:
        comisiona = seils * 0.075
    elif 1000 < seils <= 10000:
        comisiona = seils * 0.10
    elif seils > 10000:
        comisiona = seils * 0.13
    else:
        print("error")

elif town == "Plovdiv":
    if 0 <= seils <= 500:
        comisiona = seils * 0.055
    elif 500 < seils <= 1000:
        comisiona = seils * 0.08
    elif 1000 < seils <= 10000:
        comisiona = seils * 0.12
    elif seils > 10000:
        comisiona = seils * 0.145
    else:
        print("error")
else:
    print("error")

if comisiona > 0:
    print(f"{comisiona:.2f}")