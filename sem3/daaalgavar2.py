a = int(input("A toog oruul: "))
b = int(input("B toog oruul: "))
k = int(input("K toog oruul: "))

count = 0
for num in range(a, b + 1):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    if digit_sum == k:
        count += 1
        print(num_str)
print(f"bolomjit too: {count}")