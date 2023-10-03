a = [1,2,4,7,3]
max, min = a.index(max(a)), a.index(min(a))
a[max], a[min] = a[min], a[max]
print(a)