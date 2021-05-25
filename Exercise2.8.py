# Programming Exercise 2-8

# Declare variables for food charges, tip, tax, and total.
food = 0.0
tip = 0.0
tax = 0.0
total = 0.0

# Constants for the tax rate and tip rate.
TAX_RATE = 0.07
TIP_RATE = 0.18

# Get the food charges.
food = float(input("Enter the charge for food: "))

# Calculate the tip.
tip = food * TIP_RATE

# Calculate the tax.
tax = food * TAX_RATE

# Calculate the total.
total = food + tip + tax

# Print the tip, tax, and total.
print("Tip: $", format(tip, '.2f'))
print("Tax: $", format(tax, '.2f'))
print("Total: $", format(total, '.2f'))
