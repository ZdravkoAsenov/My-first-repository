length = int(input())
width = int(input())

piece = length * width

while True:
    current_piece = input()

    if current_piece == "STOP":
        print(f"{piece} pieces are left.")
        break
    if int(current_piece) <= piece:
        piece -= int(current_piece)
        if piece < 1:
            print(f"No more cake left! You need {abs(piece)} pieces more.")
            break
    else:
        print(f"No more cake left! You need {abs(piece - int(current_piece))} pieces more.")
        break
