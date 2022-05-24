username = input()
password = input()
read_password = input()

while True:
    if password != read_password:
        read_password = input()
    else:
        print(f"Welcome {username}!")
        break