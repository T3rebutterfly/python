a = str(input("ugee orrul: "))
print(a.translate({ord(i): None for i in 'b'}))