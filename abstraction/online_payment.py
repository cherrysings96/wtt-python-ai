from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self):
        self.balance = 0
        self.mode = mode

    @abstractmethod
    def pay(self, amount):
        pass

    def show(self):
        print(f"Balance={self.balance}")
        print(f"Mode is {self.mode}")


class UPI(Payment):
    def pay(self, amount):
        self.balance += amount


class CreditCard(Payment):
    def pay(self, amount):
        self.balance += amount


class DebitCard(Payment):
    def pay(self, amount):
        self.balance += amount


mode = input("Enter the mode of payment:")
if (mode == "UPI"):

    u = UPI()
    u.pay(100)
    u.show()

if (mode == "Credit Card"):
    c = CreditCard()
    c.pay(20000)
    c.show()

if (mode == "Debit Card"):
    d = DebitCard()
    d.pay(4000)
    d.show()
