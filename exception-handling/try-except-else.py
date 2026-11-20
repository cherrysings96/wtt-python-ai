try:
    user_input = int(input("Enter an integer value:"))
except ValueError:
    print("You have entered input that is not an integer!")
else:
    print(f"Success! {user_input} is an integer!")
