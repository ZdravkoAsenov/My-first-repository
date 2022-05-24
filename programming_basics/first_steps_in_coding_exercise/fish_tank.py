lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = lenght * width * height
liters = volume / 1000
busy = percent / 100
print(liters * (1 - busy))