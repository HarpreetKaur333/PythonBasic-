# Programming Exercise 3-3

# Get the person's age.
age = int(input('Enter age: '))

# Determine if the person is an infant, child,
# teenager, or adult, and display the result.
if age <= 1:
    print('Infant')
elif 1 < age < 13:
    print('Child')
elif 13 < age < 20:
    print('Teenager')
else:
    print('Adult')
