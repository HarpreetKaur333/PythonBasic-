# Programming Exercise 5-9

# Variable declarations
sales = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the total sales for the month.
sales = float(input('Enter the total sales for the month: '))

# Calculate the state sales tax.
stateTax = sales * STATE_TAX_RATE

# Calculate the county sales tax.
countyTax = sales * COUNTY_TAX_RATE

# Calculate the total tax.
totalTax = stateTax + countyTax

# Print the tax information.
print('State Tax: $', format(stateTax, ',.2f'), sep='')
print('County Tax: $', format(countyTax, ',.2f'), sep='')
print('Total Tax: $', format(totalTax, ',.2f'), sep='')



