class FirstNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 2
        return x
firstClass = FirstNumber()
firstIter = iter(firstClass)
for i in range (10):
    print(next(firstIter))