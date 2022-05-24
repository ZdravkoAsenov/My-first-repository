width = int(input())
length = int(input())
height= int(input())

volume = length * width * height

while True:
    current_box = input()

    if current_box == "Done":
        print(f"{volume} Cubic meters left.")
        break
    if int(current_box) <= volume:
        volume -= int(current_box)
        if volume < 1:
            print(f"No more free space! You need {abs(volume)} Cubic meters more.")
            break
    else:
        print(f"No more free space! You need {abs(volume - int(current_box))} Cubic meters more.")
        break