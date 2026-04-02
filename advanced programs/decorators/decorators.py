#decorators

def login(func):
    def wrapper():
        func()
        user=input("Enter the username:")
        passwrd=int(input("Enter the password:"))
        if user=="Sherene" and passwrd==1234:
            return "Login successful!"
        else:
            return "Invalid"
    return wrapper
@login
def Welcome():
    print("Welcome to Facebook!")
result=Welcome()
print(result)