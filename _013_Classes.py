class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.bRunning = False

    def Start(self):
        if self.bRunning is True:
            print("Already running")
        else:
            self.bRunning = True
            print("Started")

    def Stop(self):
        if self.bRunning is False:
            print("Already stopped")
        else:
            self.bRunning = False
            print("Stopped")

    # def __del__(self):
    #     print(f"Destroying the {self.color} {self.brand}...")
    #     print("\tNotify the Insurance...")
    #     print("\tNotify DMV...")
    #     print("\tClear to destroy")

    def __delattr__(self, instance):
        print(f"Delete an attribute of the {self.color} {self.brand}")
        super().__delattr__(instance)       ## Had forgotten this line; allow the operation forward for the deletion to actually happen.

    def __str__(self):
        return f"[{self.brand}, {self.model}, {self.year}, {self.color}]"

    def __repr__(self):
        return f"[{id(self)}: ({self.bRunning}) --> {self.brand}, {self.model}, {self.year}, {self.color}]"

    @property
    def Color(self):
        return self.color
    
    # @Color.setter
    # def Color(self, color):
    #     self.color = color


def Test1():
    c1 = Car("Toyota", "Camry", 2025, "Blue")
    c2 = Car("Honda", "Civic", 2023, "White")

    c1.Start()
    c1.Start()
    c2.Start()

    print("-"*20)
    print("Deleting attribute")
    del c1.year

    c1.vendor = "SomeShop"
    print("-"*20)
    print("Deleting object")
    print(f"{c1.__dict__ = }")
    print(f"{c2.__dict__ = }")
    del c1


    # c1.Start()


    # a = 10
    # print(a)
    # print(str(a))
    # print(a.__str__())
    # print(a.__repr__())

    print(c2)
    print(str(c2))
    print(c2.__str__())
    print(c2.__repr__())


def Test2():
    c1 = Car("Toyota", "Camry", 2025, "Blue")
    c2 = Car("Honda", "Civic", 2023, "White")

    # print(c1.GetColor())
    # c1.SetColor("Red")
    # print(c1.GetColor())

    print(c1.Color)
    c1.Color = "Black"
    print(c1.Color)

Test2()