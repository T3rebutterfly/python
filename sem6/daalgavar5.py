n = int(input("Enter Number: "))
list1 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53, 59, 67, 71, 83, 89, 101, 107, 109, 113, 127, 131, 137, 139, 149, 157, 167, 179, 181, 191, 197, 199, 211, 227, 233, 239, 251, 257, 263, 269, 281, 293, 307, 311, 317, 337, 347, 353, 359, 379, 389, 401, 409}
holder = 0
for i in range(0,len(list1)):
    for j in list1:
        if j > 1:
            for i in range(2,j//2):
                temp = j
                if(j%i==0):
                    break
                elif(n>j and temp>=j):
                    temp=j
                    holder = j
print(holder)