# 3. WAP that asks the user for age and raises exception if age is below 18

try:
    print("Vote Eligibility")
    age = int(input("Enter your age:"))
    if age >= 18:
        print("Eligible")
    elif age < 0:
        print("Enter a valid age!")
    else:
        raise ValueError(("Not eligible"))
except ValueError as e:
    print(f"Status:{e}")
else:
    print("Successful!")
finally:
    print("System check complete.")
