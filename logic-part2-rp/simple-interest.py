# Write a function to calculate simple interest:
# SI = (P × R × T) / 100
# Use a default value for rate (R = 5).
def simple_interest(principal, time, rate=5):
    si = (principal * rate * time) / 100
    return si


p = float(input("Enter principal amount:"))
t = float(input("Enter time in years:"))
r = float(
    input("Enter rate of interest (press enter to use default rate of 5%):") or 5)
interest = simple_interest(p, t, r)
print("Simple Interest:", interest)
