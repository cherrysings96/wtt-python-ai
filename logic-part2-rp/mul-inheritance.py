# Write a Python program to demonstrate multiple inheritance using:
# ●	Class Father

# ●	Class Mother

# ●	Class Child that inherits from both
# ●	 Display a method from both parent classes.


class Father:
    def father_method(self):
        return "This is the father's method."


class Mother:
    def mother_method(self):
        return "This is the mother's method."


class Child(Father, Mother):
    def child_method(self):
        return "This is the child's method."


# Create an instance of the Child class
child_instance = Child()
# Call methods from both parent classes
print(child_instance.father_method())  # Output: This is the father's method.
print(child_instance.mother_method())  # Output: This is the mother's method.
# Call the child method
print(child_instance.child_method())  # Output: This is the child's method.
