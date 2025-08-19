s1 = "Global String"

def Outer(num):

    def Inner():
        s1 = "Inner String"
        print(f"Inner --> {s1}, {num}")

    # Inner()

    s1 = "Outer String"
    print(f"Outer --> {s1}")
    return Inner

fn1 = Outer(10)
fn2 = Outer(20)
fn3 = Outer(30)


fn1()
fn2()
fn3()

print(f"Global --> {s1}")


