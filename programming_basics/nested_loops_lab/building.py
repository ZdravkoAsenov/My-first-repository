floors = int(input())
rooms = int(input())

for i in range (floors, 0, -1):
    for n in range (0, rooms):
        number_rooms = i * 10 + n
        if i == floors:
            print(f"L{number_rooms}", end=" ")
        elif i % 2 != 0:
            print(f"A{number_rooms}", end=" ")
        elif i % 2 == 0:
            print(f"O{number_rooms}", end=" ")

    print()