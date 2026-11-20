from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 1000:
            self.balance -= amount
            return self.balance
        else:
            return self.balance


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 1000:
            self.balance -= amount
            return self.balance
        else:
            return self.balance


savings = SavingsAccount(1000000)
current = CurrentAccount(1000000)

print(savings.withdraw(1200))
print(current.withdraw(900))
