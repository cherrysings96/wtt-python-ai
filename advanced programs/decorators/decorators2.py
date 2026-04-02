def Welcome(func):
    def wrapper():
        name=input("Enter the name:")
        func()
        print(name)
    return wrapper
@Welcome
def statement():
    print("Welcome to Python language,")

statement()