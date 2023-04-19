bill = int(input())
tip_percentage = float(input())
tax_percentage = float(input())

tip = bill * tip_percentage
print(f"Tip: {tip}")

tax = bill * tax_percentage
print(f'Tax: {tax}')

total = bill + tip + tax
print(f'Total: {total}')












