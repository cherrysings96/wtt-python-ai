product={"laptop":{"price":500,"quantity":3},"tv":{"price":100,"quantity":4},"radio":{"price":200,"quantity":2}}
total=0
for product,details in product.items():
    value=details["price"]*details["quantity"]
    total+=value
print(total)
