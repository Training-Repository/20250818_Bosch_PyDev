class FibGen:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self

    def __next__(self):
        if self.count < self.num:
            x = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return x
        else:
            raise StopIteration

def Test1():
    myFib = FibGen(10)
    it = iter(myFib)
    try:
        while True:
        # for _ in range(5):
            print(next(it))
    except StopIteration:
        print("Done")

def Test2():
    myFib = FibGen(10)
    # it = iter(myFib)
    # for val in it:
    for val in myFib:
        print(val)
    print("Done")

Test2()