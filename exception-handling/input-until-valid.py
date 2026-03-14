# wap that repeatedly asks the user for input until a valid number is entered
while True:
    try:
        user_input = int(input("Enter an integer:"))
    except ValueError:
        print("This is not an integer")
    else:
        print("no errors occurred")
        break
