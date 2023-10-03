b1_x = int(input("Enter the x-coordinate of bishop1: "))
b1_y = int(input("Enter the y-coordinate of bishop1: "))
b2_x = int(input("Enter the x-coordinate of bishop2: "))
b2_y = int(input("Enter the y-coordinate of bishop2: "))

bishop1 = (b1_x, b1_y)
bishop2 = (b2_x, b2_y)

if abs(b1_x - b2_x) == abs(b1_y - b2_y):
    print("The bishops can attack each other.")
else:
    print("The bishops cannot attack each other.")