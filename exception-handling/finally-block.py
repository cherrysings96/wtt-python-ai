try:
    user_input = input("Enter any input:")
except ValueError:
    print("Wrong input")
else:
    print("Correct input")
finally:
    print("Program Successful")
