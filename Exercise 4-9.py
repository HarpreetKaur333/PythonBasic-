# Programming Exercise 4-9

# Constant for the rise per year.
RISE_PER_YEAR = 1.8

# Declare a variable to store the rise.
rise = 0.0

# Calculate and print value for the rise each year.
print ('Year\t\tRise (in millimeters)')
print ('------------------------------------------')

for year in range(25):
    rise += RISE_PER_YEAR
    print ((year + 1), '\t\t', format(rise, '.2f'))

