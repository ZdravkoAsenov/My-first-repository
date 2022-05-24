best_name = ""
best_score = 0
hat_trick = False

while True:
    name = input()
    if name == "END":
        print(f"{best_name} is the best player!")
        if hat_trick:
            print(f"He has scored {best_score} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {best_score} goals.")
        break
    score = int(input())
    if score >= 10:
        print(f"{name} is the best player!")
        print(f"He has scored {score} goals and made a hat-trick !!!")
        break

    if score >= 3:
        hat_trick = True
    if best_score < score:
        best_name = name
        best_score = score
