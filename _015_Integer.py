class Integer:
    def __init__(self, data):
        try:
            self.data = int(data)
        except ValueError as ex:
            print("This type cannot be converted to an integer")
            raise

    @property
    def Data(self):
        return self.data
    
    @Data.setter
    def Data(self, val):
        self.data = val

    def __str__(self):
        return f"{self.data}"
    
    def __add__(self, other):       
        return self.data + other.data
    
    def __sub__(self, other):       
        return self.data - other.data
    
    def __gt__(self, other):
        return self.data > other.data
    

def Test1():
    var1 = Integer(30)
    var2 = Integer(20)
    print(var1, var2)

    res = var1.Data + var2.Data
    print(res)

    res = var1 + var2  #    var1.__add__(var2) --> __add__(var1, var2)
    print(res)

    res = var1 - var2
    print(res)

    if var1 > var2:
        print("Greater")
    else:
        print("Lesser")

def Test2():
    var1 = Integer("1")
    var2 = Integer("Two")

    var3 = var1 + var2
    print(var3)

Test2()