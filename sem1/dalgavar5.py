a = int(input("1duger too: "))
b = int(input("2duger too: "))
if a>=b:
    if a%2==0:
        c = a + 2
        print("daragin too bol ", c)
    else:
        c = a + 1
        print("daragin too bol ", c)
else:
    if b%2==0:
        c = b + 2
        print("daragin too bol ", c)
    else:
        c = b + 1
        print("daragin too bol ", c)
