num = int(input())
a = False
if num == 1:
    print(num, "anhnii too bish")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            a = True
            break
    if a:
        print(num, "anhnii too bish")
    else:
        print(num, "anhnii too mon")