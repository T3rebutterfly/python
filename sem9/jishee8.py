class FirstNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration
firstClass = FirstNumber()
firstIter = iter(firstClass)
for i in firstIter:
    print (i)