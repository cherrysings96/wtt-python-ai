class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)

    def withdraw(self):
        amount = int(input("Enter amount to withdraw:"))
        self.__balance -= amount
        return self.__balance

    def deposit(self):
        amount = int(input("Enter amount to deposit:"))
        self.__balance += amount
        return self.__balance


b = BankAccount(2000)

while True:
    c = int(input("Enter choice:\n(1)Check balance\n(2)Withdraw\n(3)Deposit\n(4)Exit:"))
    if c == 1:
        b.get_balance()
        continue
    elif c == 2:
        b.withdraw()
        continue
    elif c == 3:
        b.deposit()
        continue
    elif c == 4:
        break
    else:
        print("Invalid choice")
