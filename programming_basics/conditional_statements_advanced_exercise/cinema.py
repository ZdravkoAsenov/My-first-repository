type_projection = input()
row = int(input())
col = int(input())
gainings = 0

if type_projection == "Premiere":
    gainings = row * col * 12.00
    print(f"{gainings:.2f} leva")
elif type_projection == "Normal":
    gainings = row * col * 7.50
    print(f"{gainings:.2f} leva")
elif type_projection == "Discount":
    gainings = row * col * 5.00
    print(f"{gainings:.2f} leva")