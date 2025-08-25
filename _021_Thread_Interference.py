import threading
import time

class BankAccount:
    def __init__(self):
        self.bal = 0

    def deposit(self, amt):
        balance = self.bal
        time.sleep(1)       ## Deliberate delay to aloow the thread to be switched out by the scheduler
        self.bal = balance + amt
        print(f"Deposit[{amt}]: Balance[{balance} --> {self.bal}]")

    def withdraw(self, amt):
        balance = self.bal
        self.bal = balance - amt
        print(f"Withdrawl[{amt}]: Balance[{balance} --> {self.bal}]")


class BankAccountWithLocking:
    def __init__(self):
        self.bal = 0
        self.lk_bal = threading.Lock()

    def deposit(self, amt):
        with self.lk_bal:
            balance = self.bal
            time.sleep(1)       ## Deliberate delay to aloow the thread to be switched out by the scheduler
            self.bal = balance + amt
        print(f"Deposit[{amt}]: Balance[{balance} --> {self.bal}]")

    def withdraw(self, amt):
        with self.lk_bal:
            balance = self.bal
            self.bal = balance - amt
        print(f"Withdrawl[{amt}]: Balance[{balance} --> {self.bal}]")


def OperateAccount(b):
    t1 = threading.Thread(target=b.deposit, args=(100,))
    t2 = threading.Thread(target=b.withdraw, args=(50,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Final balance --> {b.bal}")


def Main():
    b1 = BankAccount()
    OperateAccount(b1)
    print("-"*25, "\n")

    b2 = BankAccountWithLocking()
    OperateAccount(b2)


Main()