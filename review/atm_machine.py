# atm machine menu driven pgm using with help of the conditional control statements
# (1) Check Balance, (2) Deposit, (3) Withdraw, (4) Exit.

choice = int(input(
    "Enter your choice:(1) Check Balance, (2) Deposit, (3) Withdraw, (4) Exit."))
balance = 1000
PIN = "1234"
pin = input("Enter PIN:")

if pin == PIN:
    if choice == 1:
        print("Balance is", balance)
    elif choice == 2:
        amt = int(input("Enter the amount you want to deposit:"))
        bal = balance+amt
        print("New balance is", bal)
    elif choice == 3:
        amt = int(input("Enter the amount you want to withdraw:"))
        bal = balance-amt
        print("New balance is", bal)
    elif choice == 4:
        exit
    else:
        print("Invalid choice")

else:
    print("Invalid PIN")
