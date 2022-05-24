number = int(input())
n = 1
flag = False

for row in range(1, number+1):
    for col in range(1, row+1):
        if n > number:
            flag = True
            break
        print(n, end=" ")
        n += 1
    print()
    if flag:
        break