import random  # Do not change or remove this line

number = random.randint(-10000, 10000)  # Random number generation

# Extract the last digit
last_digit = abs(number) % 10

# Print the required output based on the value of the last digit
print("Last digit of", number, "is", last_digit, end=' ')

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
