# Create a Payment class and override pay() method in two subclasses.
class Payment:
    def pay(self):
        return "Payment class executed"


class Bills(Payment):
    def pay(self):
        return "Bills class executed"


class Leisure(Payment):
    def pay(self):
        return "Leisure class executed"


p = Payment()
print(p.pay())
