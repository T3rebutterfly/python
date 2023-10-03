a = int(input("A toog oruul: "))
b = int(input("B toog oruul: "))
for s in range(1,a):
    for sl in range(1,a):
        if(s * sl == a):
            print("A giin urjver",s ,"B",sl)
for s in range(1,b):
    for sl in range(1,b):
        if(s * sl == b):
            print("B giin urjver",s,"B",sl)