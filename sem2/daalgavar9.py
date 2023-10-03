n = int(input())
for i in range(1,n+1):
    txt = str(i)
    txt = txt[::-1]
    too = int(txt)
    if i == too:
        print(i)