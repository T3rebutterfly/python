n = 0
for i in range(0,1000):
    n += 1
    s = str(i)
    b = len(s)
    c = str(n)
    if(b == 3 and c == c[::-1]):
        print(c)