international_shipping = True

total = int(input('Enter total amount: '))
shipping_cost = 0

if international_shipping:
    shipping_cost += 15
    print('International base cost aplied')

if total <= 50:
    shipping_cost += 20
elif total <= 100:
    shipping_cost += 15
else:
    shipping_cost += 5

print(f"Shipping cost: {shipping_cost}")
