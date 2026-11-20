import functools

# 1. INHERITANCE + ENCAPSULATION
class Product:
    def __init__(self, name, price):
        self.__price = price   # private variable
        self.name = name

    def get_price(self):
        return self.__price


# 2. POLYMORPHISM
class FoodItem(Product):
    def describe(self):
        return f"🍔 {self.name:10} | ${self.get_price()}"


class DrinkItem(Product):
    def describe(self):
        return f"🥤 {self.name:10} | ${self.get_price()} (Includes Ice)"


# 3. ABSTRACTION (User interacts only with this system)
class OrderingSystem:
    def __init__(self):
        self.menu = [
            FoodItem("Burger", 10),
            FoodItem("Pizza", 15),
            DrinkItem("Soda", 2)
        ]
        self.cart = []

    def run(self):
        print("Welcome to Python Diner!")

        while True:
            print("\n1. View Menu  2. Add Item  3. Checkout & Exit")
            cmd = input("Choose (1-3): ")

            if cmd == "1":
                # GENERATOR
                for item in (i.describe() for i in self.menu):
                    print(item)

            elif cmd == "2":
                self.add_to_cart()

            elif cmd == "3":
                self.checkout()
                break

            else:
                print("Invalid choice!")

    def add_to_cart(self):
        try:
            choice = input("Enter item name: ").capitalize()

            # LIST COMPREHENSION
            match = [i for i in self.menu if i.name == choice]

            if not match:
                raise ValueError(f"{choice} not found!")

            self.cart.append(match[0])
            print(f"✅ {choice} added!")

        except ValueError as e:
            print(f"❌ {e}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty!")
            return

        # MAP + LAMBDA
        prices = list(map(lambda x: x.get_price(), self.cart))

        # REDUCE
        total = functools.reduce(lambda a, b: a + b, prices)

        print("\n--- BILL ---")
        print("Items:", ", ".join([i.name for i in self.cart]))
        print("Total: $", total)

        # FILE HANDLING
        with open("bill.txt", "w") as f:
            f.write(f"Items: {', '.join([i.name for i in self.cart])}\n")
            f.write(f"Total: ${total}")

        print("🧾 Bill saved to bill.txt")


# --- RUN ---
app = OrderingSystem()
app.run()