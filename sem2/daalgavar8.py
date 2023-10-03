num = int(input())
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "Anhnii too bish")
        else:
            print(num, "Anhnii too mon")
        break
else:
    print(num, "Anhnii too bish")